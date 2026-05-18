from fastapi import (
    APIRouter,
    Depends
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from sqlalchemy.orm import Session

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

# Enables Swagger Authorize
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

    return {
        "total_live_threats":
            len(active_threats),
        "threats":
            active_threats
    }


@router.get("/analytics/summary")
def summary(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    threats = db.query(Threat).all()

    return {
        "critical": len([
            t for t in threats
            if t.severity == "Critical"
        ]),
        "high": len([
            t for t in threats
            if t.severity == "High"
        ]),
        "medium": len([
            t for t in threats
            if t.severity == "Medium"
        ]),
        "low": len([
            t for t in threats
            if t.severity == "Low"
        ])
    }