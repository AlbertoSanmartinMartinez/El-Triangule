from typing import ClassVar

from uuid import uuid4, UUID

from datetime import datetime

from pydantic import BaseModel, Field


class CustomModel(BaseModel):
    """
    Model base with UUID primary key
    """
    
    pk_field: ClassVar[str] = "uuid"

    uuid: UUID = Field(default_factory=lambda: uuid4())

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }


class TenantModel(CustomModel):
    """
    Model base with tenant_id field for multi-tenant support
    """

    tenant_id: None | str = None