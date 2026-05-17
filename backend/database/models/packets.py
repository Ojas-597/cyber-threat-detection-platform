from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)

from backend.database.base import Base


class Packet(Base):
    __tablename__ = "packets"

    packet_id = Column(
        String,
        primary_key=True,
        index=True
    )

    source_ip = Column(
        String,
        nullable=False
    )

    destination_ip = Column(
        String,
        nullable=False
    )

    protocol = Column(
        String,
        nullable=False
    )

    packet_size = Column(
        Integer
    )

    risk_score = Column(
        Integer
    )

    captured_at = Column(
        DateTime,
        default=datetime.utcnow
    )
