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

from backend.database.models.packets import (
    Packet
)

router = APIRouter(
    prefix="/packets",
    tags=["Packets"]
)

# Enables Swagger Authorize
security = HTTPBearer()


@router.get("/")
def packets(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    packet_records = (
        db.query(Packet)
        .all()
    )

    return {
        "message":
            "Packet monitoring endpoint",
        "count":
            len(packet_records),
        "packets":
            packet_records
    }