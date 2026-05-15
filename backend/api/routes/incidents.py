from fastapi import APIRouter

router = APIRouter(
    prefix="/incidents",
    tags=["Incident Response"]
)

@router.get("/")
def get_incidents():

    return {
        "message": "Incident response endpoint"
    }
