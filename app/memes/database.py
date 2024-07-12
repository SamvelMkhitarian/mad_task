from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.memes.settings import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

DATABASE_URL_MEMES = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
# DATABASE_URL_MEMES = 'postgresql+asyncpg://postgres:password@postgreshost:5433/memes'

engine = create_async_engine(DATABASE_URL_MEMES)
SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db_memes():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
