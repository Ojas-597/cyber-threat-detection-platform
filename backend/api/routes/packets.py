from fastapi import APIRouter

router = APIRouter(
    prefix="/packets",
    tags=["Packets"]
)

@router.get("/")
def get_packets():

    return {
        "message": "Packet monitoring endpoint"
    }
