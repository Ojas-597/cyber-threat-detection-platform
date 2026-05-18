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

from backend.database.models.incidents import (
    Incident
)

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)

# Enables Swagger "Authorize"
security = HTTPBearer()


@router.get("/")
def get_incidents(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    incidents = (
        db.query(Incident)
        .all()
    )

    return {
        "count":
            len(incidents),
        "incidents":
            incidents
    }