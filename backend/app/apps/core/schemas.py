from pydantic import BaseModel, Field


class IdSchema(BaseModel):
    id: int = Field(description="User ID", example=1, gt=0,)