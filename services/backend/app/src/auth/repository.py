from sqlalchemy import select

from app.src.base.repository import BaseRepository
from app.src.database import async_session_maker
from app.src.auth.models import User
from app.src.auth.schemas import UserSchema


class UserRepository(BaseRepository[User]):

    def __init__(self):
        super().__init__(
            model=User,
            schema=UserSchema
        )

    async def get_by_email(self, email: str) -> User | None:
        async with async_session_maker() as session:
            result = await session.execute(
                select(UserSchema).where(UserSchema.email == email)
            )
            db_user = result.scalar_one_or_none()
            if db_user is None:
                return None
            return self._to_user(db_user)

    @staticmethod
    def _to_user(db_user: UserSchema) -> User:
        return User(
            uuid=db_user.uuid,
            email=db_user.email,
            password=db_user.password,
            is_active=db_user.is_active,
            role=db_user.role,
        )
