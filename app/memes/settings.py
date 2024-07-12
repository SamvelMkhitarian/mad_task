from dotenv import load_dotenv
import os
import pathlib

ROOT_PATH = pathlib.Path(__file__).resolve().parent.parent.parent
load_dotenv((ROOT_PATH / '.env.nemes').as_posix())

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
MEDIA_SERVICE_URL = os.getenv('MEDIA_SERVICE_URL')
