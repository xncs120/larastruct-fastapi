import os

PG_HOST = os.getenv("PG_DB_HOST") or ""
PG_USER = os.getenv("PG_DB_USER") or ""
PG_PASSWORD = os.getenv("PG_DB_PASSWORD") or ""
PG_NAME = os.getenv("PG_DB_NAME") or ""

class Settings:
    PROJECT_NAME: str = "App"
    DATABASE_URL: str = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_NAME}"
    SECRET_KEY: str = os.getenv("SECRET_KEY") or "" # openssl rand -hex 32
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

settings = Settings()