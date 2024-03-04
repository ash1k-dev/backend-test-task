import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv(
    "DB_URL", default="postgresql+asyncpg://postgres:postgres@localhost/axon"
)
DB_URL_TEST = os.getenv(
    "DB_URL_TEST", default="postgresql+asyncpg://postgres:postgres@localhost/axon_test"
)
