from fastapi import Depends, UploadFile, File, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from minio.error import S3Error

from app.media.client import client, bucket_name
from app.media.models import File as FileModel
from app.media.database import get_db_media
from app.media.schemas import FileSchema
from app.media.settings import MINIO_URL

router = APIRouter(prefix="/api")


@router.post("/upload", response_model=FileSchema)
async def upload_file(file: UploadFile = File(...), db: AsyncSession = Depends(get_db_media)):
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    try:
        client.put_object(
            bucket_name, file.filename, file.file, length=-1, part_size=10*1024*1024,
            content_type=file.content_type
        )
    except S3Error as e:
        raise HTTPException(status_code=500, detail=str(e))

    new_file = FileModel(
        file=f"{MINIO_URL}/{bucket_name}/{file.filename}",
        file_name=file.filename,
        content_type=file.content_type,
        size=file.size
    )
    db.add(new_file)
    await db.commit()
    return new_file
