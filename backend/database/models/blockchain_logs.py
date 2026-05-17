from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime
)

from backend.database.base import Base


class BlockchainLog(Base):
    __tablename__ = "blockchain_logs"

    log_id = Column(
        String,
        primary_key=True,
        index=True
    )

    event_hash = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    event_type = Column(
        String,
        nullable=False
    )

    anchored = Column(
        Boolean,
        default=True,
        nullable=False
    )

    blockchain_tx_hash = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
