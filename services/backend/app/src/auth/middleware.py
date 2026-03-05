from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.src.auth.jwt import decode_token
from app.src.config import settings


PUBLIC_PATHS = (
    f"/{settings.api_prefix}/health",
    f"/{settings.api_prefix}/docs",
    f"/{settings.api_prefix}/redoc",
    f"/{settings.api_prefix}/openapi.json",
    f"/{settings.api_prefix}/auth/user/register",
    f"/{settings.api_prefix}/auth/user/login",
    f"/{settings.api_prefix}/auth/user/refresh",
)


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> Response:
        path = request.url.path

        if any(path == p or path.startswith(p) for p in PUBLIC_PATHS):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Missing authentication token"})

        token = auth_header.removeprefix("Bearer ").strip()

        try:
            payload = decode_token(token)
        except Exception:
            return JSONResponse(status_code=401, content={"detail": "Invalid or expired token"})

        if payload.get("type") != "access":
            return JSONResponse(status_code=401, content={"detail": "Invalid token type"})

        request.state.user_uuid = payload["sub"]
        request.state.role = payload.get("role", "user")

        return await call_next(request)
