from sqlalchemy import Column, String, Boolean, Enum as SA_Enum

from app.src.database import Base
from app.src.base.schema import CustomSchema
from app.src.auth.models import Role


class UserSchema(CustomSchema, Base):
    __tablename__ = "auth__user"

    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    role = Column(SA_Enum(Role, name="auth__role", native_enum=True), default=Role.USER, nullable=False)
