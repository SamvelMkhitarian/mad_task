from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.memes.database import engine
from app.media.routers import router
from app.media import models

media_app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield

media_app.router.lifespan = lifespan

media_app.include_router(router)
