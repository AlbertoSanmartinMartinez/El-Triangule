from app.src.base.repository import BaseRepository
from app.src.images.models import Album, Image
from app.src.images.schemas import AlbumSchema, ImageSchema


class AlbumRepository(BaseRepository[Album]):

    def __init__(self):
        super().__init__(
            model=Album,
            schema=AlbumSchema
        )


class ImageRepository(BaseRepository[Image]):

    def __init__(self):
        super().__init__(
            model=Image,
            schema=ImageSchema
        )
