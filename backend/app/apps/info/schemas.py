from pydantic import BaseModel, Field


class BackendInfo(BaseModel):
    backend: str = Field(description="Backend hostname")


class DatabaseInfo(BaseModel):
    database: str = Field(description="Database URL")
