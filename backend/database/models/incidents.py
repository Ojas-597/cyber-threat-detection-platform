from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey
)

from backend.database.base import Base


class Incident(Base):
    __tablename__ = "incidents"

    incident_id = Column(
        String,
        primary_key=True,
        index=True
    )

    threat_id = Column(
        String,
        ForeignKey(
            "threats.threat_id"
        ),
        nullable=False
    )

    severity = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="open"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
