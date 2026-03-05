import os
import shutil
from uuid import uuid4

from fastapi import Request, UploadFile

from app.src.base.controller import BaseController
from app.src.images.models import Album, Image
from app.src.images.repository import AlbumRepository, ImageRepository

MEDIA_DIR = "/app/media"


class AlbumController(BaseController[Album]):

    def __init__(self):
        super().__init__(
            repository=AlbumRepository(),
            event=None,
            cache=None
        )


class ImageController(BaseController[Image]):

    def __init__(self):
        super().__init__(
            repository=ImageRepository(),
            event=None,
            cache=None
        )

    async def create(self, item: Image, request: Request | None = None) -> Image:
        os.makedirs(MEDIA_DIR, exist_ok=True)

        file: UploadFile | None = getattr(request.state, "file", None) if request else None
        if file:
            ext = os.path.splitext(file.filename or "file")[1]
            filename = f"{uuid4()}{ext}"
            filepath = os.path.join(MEDIA_DIR, filename)

            with open(filepath, "wb") as f:
                shutil.copyfileobj(file.file, f)

            item.media_type = "video" if ext.lower() in (".mp4", ".webm", ".mov", ".avi") else "image"
            item.file_url = f"/media/{filename}"

        return await self.repository.create(item)
