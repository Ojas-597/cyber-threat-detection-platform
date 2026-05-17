from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime
)

from backend.database.base import Base


class Threat(Base):
    __tablename__ = "threats"

    threat_id = Column(
        String,
        primary_key=True,
        index=True
    )

    type = Column(
        String,
        nullable=False
    )

    severity = Column(
        String,
        nullable=False
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

    status = Column(
        String,
        nullable=False
    )

    mitre_attack_id = Column(
        String
    )

    confidence_score = Column(
        Float
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
