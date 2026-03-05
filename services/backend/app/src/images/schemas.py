from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.src.database import Base
from app.src.base.schema import CustomSchema, TimestampSchema, OwnerSchema


class AlbumSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "images__album"

    name = Column(String(255), nullable=False)
    cover_image_url = Column(String(500), nullable=True)
    event_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("events__event.uuid"), nullable=True, index=True)


class ImageSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "images__image"

    album_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("images__album.uuid"), nullable=False, index=True)
    file_url = Column(String(500), nullable=False)
    thumbnail_url = Column(String(500), nullable=True)
    media_type = Column(String(20), default="image", nullable=False)
