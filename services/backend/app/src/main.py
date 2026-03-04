from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.src.database import async_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    yield
    await async_engine.dispose()


app = FastAPI(title="Backend", lifespan=lifespan)


@app.get("/")
async def health_check():
    return {"status": "ok"}
