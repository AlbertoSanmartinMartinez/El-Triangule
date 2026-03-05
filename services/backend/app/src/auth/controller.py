from app.src.base.controller import BaseController
from app.src.auth.models import (
    User,
    LoginRequest,
    RegisterRequest,
    RefreshRequest,
    TokenResponse,
)
from app.src.auth.repository import UserRepository
from app.src.auth.password import hash_password, verify_password
from app.src.auth.jwt import create_access_token, create_refresh_token, decode_token
from app.src.base.error import ConflictError, UnauthorizedError


class AuthController(BaseController[User]):

    def __init__(self):
        super().__init__(
            repository=UserRepository(),
            event=None,
            cache=None
        )

    async def register(self, data: RegisterRequest) -> TokenResponse:
        existing = await self.repository.get_by_email(data.email)
        if existing is not None:
            raise ConflictError("Email already registered")

        user = User(
            email=data.email,
            password=hash_password(data.password),
        )
        user = await self.repository.create(user)

        return self._build_tokens(user)

    async def login(self, data: LoginRequest) -> TokenResponse:
        user = await self.repository.get_by_email(data.email)
        if user is None or not verify_password(data.password, user.password):
            raise UnauthorizedError("Invalid email or password")

        if not user.is_active:
            raise UnauthorizedError("Account is disabled")

        return self._build_tokens(user)

    async def refresh(self, data: RefreshRequest) -> TokenResponse:
        payload = decode_token(data.refresh_token)
        if payload.get("type") != "refresh":
            raise UnauthorizedError("Invalid refresh token")

        user = await self.repository.detail(payload["sub"])
        if not user.is_active:
            raise UnauthorizedError("Account is disabled")

        return self._build_tokens(user)

    @staticmethod
    def _build_tokens(user: User) -> TokenResponse:
        token_data = {"sub": str(user.uuid), "role": user.role.value}
        return TokenResponse(
            access_token=create_access_token(token_data),
            refresh_token=create_refresh_token(token_data),
        )
