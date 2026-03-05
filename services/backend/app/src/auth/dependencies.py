from fastapi import Request, HTTPException, status

from app.src.auth.models import Role

ROLE_HIERARCHY = [Role.ADMIN, Role.BOARD, Role.PARTNER, Role.USER]


def require_role(minimum_role: Role):
    async def _check(request: Request) -> None:
        user_role_value: str = getattr(request.state, "role", Role.USER.value)
        try:
            user_role = Role(user_role_value)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid role",
            )
        if ROLE_HIERARCHY.index(user_role) > ROLE_HIERARCHY.index(minimum_role):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
    return _check
