from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE")
DB_SCHEMA = os.getenv("DB_SCHEMA")
DB_TABLE = os.getenv("DB_TABLE")


def get_connection():
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()