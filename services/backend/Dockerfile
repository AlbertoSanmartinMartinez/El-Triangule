FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml .
RUN uv sync --no-dev --no-install-project

COPY alembic.ini .
COPY app/ app/

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
