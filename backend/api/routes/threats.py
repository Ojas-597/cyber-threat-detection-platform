from fastapi import (
    APIRouter,
    Depends
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from sqlalchemy.orm import Session
import random

from backend.database.connection import (
    get_db
)

from backend.database.models.threats import (
    Threat
)

router = APIRouter(
    prefix="/threats",
    tags=["Threats"]
)

security = HTTPBearer()


@router.get("/live")
def get_live_threats(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    active_threats = (
        db.query(Threat)
        .filter(
            Threat.status == "Active"
        )
        .all()
    )

    real_count = len(active_threats)

    # Add random fluctuation for demo
    simulated_count = real_count + random.randint(0, 3)

    return {
        "total_live_threats": simulated_count,
        "threats": active_threats
    }


@router.get("/analytics/summary")
def summary(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    threats = db.query(Threat).all()

    critical = len([
        t for t in threats
        if t.severity == "Critical"
    ])

    high = len([
        t for t in threats
        if t.severity == "High"
    ])

    medium = len([
        t for t in threats
        if t.severity == "Medium"
    ])

    low = len([
        t for t in threats
        if t.severity == "Low"
    ])

    return {
        "critical": critical + random.randint(0, 2),
        "high": high + random.randint(0, 2),
        "medium": medium + random.randint(0, 2),
        "low": low + random.randint(0, 1)
    }