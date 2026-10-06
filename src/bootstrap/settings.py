from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PgSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    db: str = "project_name"
    user: str = "project_name"
    password: str = "project_name"

    @property
    def sqlalchemy_url(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        )


class RedisSettings(BaseModel):
    host: str = "localhost"
    port: int = 6379
    db: int = 0
    password: str | None = None


class RmqSettings(BaseModel):
    rabbit_broker_url: str = "amqp://guest:guest@localhost:5672/"


class S3Settings(BaseModel):
    endpoint_url: str = "http://localhost:9000"
    access_key_id: str = "minioadmin"
    secret_access_key: str = "minioadmin"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".dev.env",
        env_nested_delimiter="__",
        extra="ignore",
    )

    pg: PgSettings = Field(default_factory=PgSettings)
    redis: RedisSettings = Field(default_factory=RedisSettings)
    rmq: RmqSettings = Field(default_factory=RmqSettings)
    s3: S3Settings = Field(default_factory=S3Settings)
