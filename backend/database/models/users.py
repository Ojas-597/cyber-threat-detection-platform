from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime
)

from backend.database.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(
        String,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )

    mfa_enabled = Column(
        Boolean,
        default=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
