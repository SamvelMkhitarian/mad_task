from sqlalchemy_utils import create_database, drop_database
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import tempfile
import pytest
import os

from app.memes.database import Base, get_db_memes
from app.memes.settings import settings
from app.memes.main import app

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL_MEMES

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    create_database(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    yield
    drop_database(SQLALCHEMY_DATABASE_URL)


@pytest.fixture(autouse=True)
async def clear_database():
    async with engine.begin() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            await conn.execute(table.delete())
    yield


@pytest.fixture
async def db_session():
    async with TestingSessionLocal() as session:
        yield session


async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db_memes] = override_get_db

client = TestClient(app)


def test_create_meme(db_session):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(b"Test content")
        tmp_file_name = tmp_file.name

    with open(tmp_file_name, "rb") as file:
        response = client.post(
            "/upload",
            files={"file": (file.name, file, "image/jpeg")}
        )

    os.remove(tmp_file_name)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["file_name"] == os.path.basename(tmp_file_name)
    assert response_data["content_type"] == "image/jpeg"
    assert response_data["file"].startswith("http://localhost:9000/")

    file = response_data["file"]
    response = client.post(
        "/memes", json={"title": "Test Meme", "image_url": file}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Meme"
    assert response.json()["image_url"] == file


@pytest.fixture
def create_memes(db_session):
    memes = [
        {"title": "Test Meme 1", "image_url": "http://example.com/test1.jpg"},
        {"title": "Test Meme 2", "image_url": "http://example.com/test2.jpg"}
    ]
    for meme in memes:
        response = client.post("/memes", json=meme)
        assert response.status_code == 201
    return memes


def test_read_memes(db_session, create_memes):
    response = client.get("/memes")
    assert response.status_code == 200
    assert len(response.json()) == len(create_memes)


def test_read_meme(db_session, create_memes):
    meme_id = client.post("/memes", json=create_memes[0]).json()["id"]

    response = client.get(f"/memes/{meme_id}")
    assert response.status_code == 200
    assert response.json()["id"] == meme_id
