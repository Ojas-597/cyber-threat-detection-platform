from backend.database.base import Base
from backend.database.connection import engine

# Import models so SQLAlchemy registers them
from backend.database.models import (
    users,
    threats,
    incidents,
    packets,
    blockchain_logs
)


def init_database():
    Base.metadata.create_all(
        bind=engine
    )
