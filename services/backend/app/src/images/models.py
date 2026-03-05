from app.src.base.model import CustomModel, TimestampModel, OwnerModel


class Album(CustomModel, TimestampModel, OwnerModel):
    name: str
    cover_image_url: str | None = None
    event_uuid: str | None = None


class Image(CustomModel, TimestampModel, OwnerModel):
    album_uuid: str
    file_url: str
    thumbnail_url: str | None = None
    media_type: str = "image"
