import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
DB_URL_TEST = os.getenv("DB_URL_TEST")
