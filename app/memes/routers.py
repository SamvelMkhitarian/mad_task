from fastapi import Depends, File, Form, HTTPException, UploadFile, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.memes.database import get_db_memes
from app.memes import queries
from app.memes import schemas

router = APIRouter(prefix="/api")


@router.get("/memes", response_model=List[schemas.Meme])
async def read_memes(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db_memes)):
    memes = await queries.get_memes(db, skip=skip, limit=limit)
    return memes


@router.get("/memes/{meme_id}", response_model=schemas.Meme)
async def read_meme(meme_id: int, db: AsyncSession = Depends(get_db_memes)):
    db_meme = await queries.get_meme(db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme


@router.post("/memes", response_model=schemas.Meme, status_code=status.HTTP_201_CREATED)
async def create_meme(title: str = Form(), file: UploadFile = File(...), db: AsyncSession = Depends(get_db_memes)):
    meme = schemas.MemeCreate(title=title)
    return await queries.create_meme(db=db, meme=meme, file=file)


@router.put("/memes/{meme_id}", response_model=schemas.Meme)
async def update_meme(meme_id: int, meme: schemas.MemeCreate, db: AsyncSession = Depends(get_db_memes)):
    return await queries.update_meme(db=db, meme_id=meme_id, meme=meme)


@router.delete("/memes/{meme_id}", response_model=schemas.Meme)
async def delete_meme(meme_id: int, db: AsyncSession = Depends(get_db_memes)):
    return await queries.delete_meme(db=db, meme_id=meme_id)
