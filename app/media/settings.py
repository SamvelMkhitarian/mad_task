from dotenv import load_dotenv
import os
import pathlib

ROOT_PATH = pathlib.Path(__file__).resolve().parent.parent.parent
load_dotenv((ROOT_PATH / '.env.media').as_posix())


POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

MINIO_ROOT_USER = os.getenv('MINIO_ROOT_USER')
MINIO_ROOT_PASSWORD = os.getenv('MINIO_ROOT_PASSWORD')
MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT')
MINIO_BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME')
MINIO_SECURE = os.getenv('MINIO_SECURE')

# MINIO_KEY = os.getenv('MINIO_KEY')
# MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')

MINIO_URL = os.getenv('MINIO_URL')

DATABASE_URL_MEDIA = os.getenv('DATABASE_URL_MEDIA')
