from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database file
DATABASE_URL = "sqlite:///./cyber_threat.db"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    """
    FastAPI database dependency.
    Creates a session for each request
    and closes it automatically.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
