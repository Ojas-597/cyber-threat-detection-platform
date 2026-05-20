from fastapi import APIRouter, Depends
from backend.authentication.dependencies import get_current_user
from backend.intrusion_detection.service import detect_intrusion

router = APIRouter(
    prefix="/intrusion",
    tags=["Intrusion Detection"]
)

@router.post("/check")
def check_intrusion(
    data: dict,
    current_user=Depends(get_current_user)
):
    return detect_intrusion(data["ip"])