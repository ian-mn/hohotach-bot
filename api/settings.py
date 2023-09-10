import os

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = Field("Memes API", env="API_NAME")
    LOGGING_LEVEL: str = Field("DEBUG", env="LOGGING_LEVEL")
    BASE_DIR: str = Field(os.path.dirname(os.path.abspath(__file__)))
    DISLIKE_SHARE_THRESHOLD: float = Field(0.9)


class DBSettings(BaseSettings):
    user: str = Field("parser", env="DB_USER")
    password: str = Field("123qwe", env="DB_PASS")
    host: str = Field("db", env="DB_HOST")
    port: int = Field(5432, env="DB_PORT")
    dbname: str = Field("memes", env="DB_NAME")


settings = Settings()
db_settings = DBSettings()
