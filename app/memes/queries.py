from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import List, Optional
from fastapi import UploadFile
import aiohttp

from app.memes.settings import MEDIA_SERVICE_URL
from app.memes import models, schemas


async def upload_file(file: UploadFile) -> dict:
    async with aiohttp.ClientSession() as session:
        url = f"{MEDIA_SERVICE_URL}/upload"
        print(url)
        form = aiohttp.FormData()
        form.add_field('file', file.file, filename=file.filename,
                       content_type=file.content_type)
        async with session.post(url, data=form) as response:
            response.raise_for_status()
            return await response.json()


async def get_meme(db: AsyncSession, meme_id: int) -> Optional[models.Meme]:
    stmt = select(models.Meme).where(models.Meme.id == meme_id)
    result = await db.execute(stmt)
    return result.scalars().first()


async def get_memes(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[models.Meme]:
    stmt = select(models.Meme).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def create_meme(db: AsyncSession, meme: schemas.MemeCreate, file: UploadFile) -> models.Meme:
    upload_response = await upload_file(file)
    memes_data = meme.model_dump()
    memes_data['file_id'] = upload_response['id']
    db_meme = models.Meme(**memes_data)
    db.add(db_meme)
    await db.commit()
    return db_meme


async def update_meme(db: AsyncSession, meme_id: int, meme: schemas.MemeCreate) -> Optional[models.Meme]:
    stmt = (
        update(models.Meme)
        .where(models.Meme.id == meme_id)
        .values(**meme.model_dump())
        .returning(models.Meme)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


async def delete_meme(db: AsyncSession, meme_id: int) -> Optional[models.Meme]:
    stmt = (
        delete(models.Meme)
        .where(models.Meme.id == meme_id)
        .returning(models.Meme)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()
