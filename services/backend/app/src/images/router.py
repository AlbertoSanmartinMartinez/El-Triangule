from app.src.base.router import BaseRouter
from app.src.config import settings
from app.src.images.models import Album, Image
from app.src.images.controller import AlbumController, ImageController

album_router: BaseRouter[Album] = BaseRouter(
    model=Album,
    controller=AlbumController,
    prefix=f"/{settings.api_prefix}/images/album",
    tags=["Album"],
)

image_router: BaseRouter[Image] = BaseRouter(
    model=Image,
    controller=ImageController,
    prefix=f"/{settings.api_prefix}/images/image",
    tags=["Image"],
)
