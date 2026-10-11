from sqlalchemy import String, Boolean, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, validates
from datetime import datetime, UTC

from app.common.models import BaseModel


class User(BaseModel):
    __tablename__="users"

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    hashed_password: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default=text("true"),
    )

    is_verified:Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=text("false"),
    )

    last_login_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    @validates("email")
    def _normalize_email(self, _key:str, value: str) -> str:
        return value.strip.lower()

    def __repr__(self):
        return f'User Id= {self.id}, email={self.email}'

class RefreshToken(BaseModel):
    __tablename__ = "refresh_tokens"
    user_id: Mapped[str] = mapped_column(index=True)
    token_hash: Mapped[str] = mapped_column(unique=True, index=True)
    expires_at: Mapped[datetime]
    revoked: Mapped[bool] = mapped_column(default=False)