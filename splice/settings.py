from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    # Database
    DATABASE_URL: str = 'postgres'
    DATABASE_URL_TEST: str = 'postgres'

    # JWT
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    JWT_ALGORITHM: str = 'HS256'
    JWT_SECRET_KEY: str

    # Log
    LOG_LEVEL: str = 'DEGUB'

    OPENAPI_URL: str = '/openapi.json'


settings = Settings()
