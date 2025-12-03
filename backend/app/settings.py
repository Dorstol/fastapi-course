from functools import lru_cache

from pydantic_settings import BaseSettings


class CoreSettings(BaseSettings):
    APP_NAME: str = "Title"
    DEBUG: bool = False


class PostgreSQLSettings(BaseSettings):
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int = 5432

    @property
    def database_async_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"
        )


class Settings(CoreSettings, PostgreSQLSettings):
    pass


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
