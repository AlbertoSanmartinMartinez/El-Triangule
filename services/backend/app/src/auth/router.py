from fastapi import HTTPException

from app.src.base.router import BaseRouter
from app.src.base.error import AppError
from app.src.config import settings
from app.src.auth.models import (
    User,
    LoginRequest,
    RegisterRequest,
    RefreshRequest,
    TokenResponse,
)
from app.src.auth.controller import AuthController

user_router: BaseRouter[User] = BaseRouter(
    model=User,
    controller=AuthController,
    prefix=f"/{settings.api_prefix}/auth/user",
    tags=["User"],
)


@user_router.router.post(
    "/register",
    status_code=201,
    response_model=TokenResponse,
    summary="User register",
)
async def register(data: RegisterRequest) -> TokenResponse:
    try:
        return await user_router.controller.register(data)
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@user_router.router.post(
    "/login",
    response_model=TokenResponse,
    summary="User login",
)
async def login(data: LoginRequest) -> TokenResponse:
    try:
        return await user_router.controller.login(data)
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@user_router.router.post(
    "/refresh",
    response_model=TokenResponse,
    summary="Refresh token",
)
async def refresh(data: RefreshRequest) -> TokenResponse:
    try:
        return await user_router.controller.refresh(data)
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
