from fastapi import APIRouter, Depends
from backend.authentication.dependencies import get_current_user
from backend.intrusion_detection.service import detect_intrusions

router = APIRouter(
    prefix="/intrusion",
    tags=["Intrusion Detection"]
)

@router.get("")
def get_intrusions(
    current_user=Depends(get_current_user)
):
    return detect_intrusions()