from fastapi import (
    APIRouter,
    Depends
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


@router.get("/")
def packets(
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
