from typing import ClassVar

from uuid import uuid4, UUID

from datetime import datetime

from pydantic import BaseModel, Field


class CustomModel(BaseModel):
    pk_field: ClassVar[str] = "uuid"

    uuid: UUID = Field(default_factory=lambda: uuid4())

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }


class TimestampModel(BaseModel):
    created_at: datetime | None = None
    updated_at: datetime | None = None


class OwnerModel(BaseModel):
    created_by: str | None = None
