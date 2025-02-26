from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    # Database
    DATABASE_URL: str = (
        'postgresql+asyncpg://postgres:root@localhost:5432/splice'
    )
    DATABASE_URL_TEST: str = 'postgres'
    MONGO_DB_NAME: str = 'splice'
    MONGO_URL: str = 'mongodb://localhost:27017/splice'

    # JWT
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    JWT_ALGORITHM: str = 'HS256'
    JWT_SECRET_KEY: str = 'qualquer_texto'

    # Log
    LOG_LEVEL: str = 'DEGUB'

    OPENAPI_URL: str = '/openapi.json'


settings = Settings()
