from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.media.settings import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

DATABASE_URL_MEDIA = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
# DATABASE_URL_MEDIA = 'postgresql+asyncpg://postgres:password@postgreshost:5433/media'

# POSTGRES_DB_MEDIA=media
# POSTGRES_USER_MEDIA=postgres
# POSTGRES_PASSWORD_MEDIA=password
# POSTGRES_HOST_MEDIA=postgreshost
# POSTGRES_PORT_MEDIA=5433


engine = create_async_engine(DATABASE_URL_MEDIA)
SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db_media():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
