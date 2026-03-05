from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text

from app.src.config import settings
from app.src.database import async_engine
from app.src.auth.middleware import AuthMiddleware
from app.src.auth.router import user_router
from app.src.events.router import event_router
from app.src.notifications.router import notification_router
from app.src.images.router import album_router, image_router
from app.src.payments.router import payment_router
from app.src.messages.router import conversation_router, message_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    yield
    await async_engine.dispose()


app = FastAPI(
    title="El Triangule API",
    description="REST API for El Triangule",
    version=settings.version,
    lifespan=lifespan,
    docs_url=f"/{settings.api_prefix}/docs",
    redoc_url=f"/{settings.api_prefix}/redoc",
    openapi_url=f"/{settings.api_prefix}/openapi.json",
    separate_input_output_schemas=False,
)

app.add_middleware(AuthMiddleware)

app.include_router(user_router.router)
app.include_router(event_router.router)
app.include_router(notification_router.router)
app.include_router(album_router.router)
app.include_router(image_router.router)
app.include_router(payment_router.router)
app.include_router(conversation_router.router)
app.include_router(message_router.router)

app.mount("/media", StaticFiles(directory="/app/media"), name="media")


@app.get(f"/{settings.api_prefix}/health")
async def health_check():
    return {"status": "ok"}
