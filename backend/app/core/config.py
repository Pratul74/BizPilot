from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from functools import lru_cache

BASE_DIR=Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    PROJECT_NAME: str
    TELEGRAMBOT_TOKEN: str
    DATABASE_URL: str
    REDIS_URL:str
    RABBITMQ_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    ENVIRONMENT:str = "development"

    DB_MAX_OVERFLOW: int
    DB_POOL_size: int


    model_config = SettingsConfigDict(
        env_file=BASE_DIR/".env",
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()