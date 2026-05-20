from fastapi import APIRouter, Depends
from backend.authentication.dependencies import get_current_user
from backend.phishing_detection.service import check_url

router = APIRouter(
    prefix="/phishing",
    tags=["Phishing"]
)

@router.post("/check")
def check_phishing(
    data: dict,
    current_user=Depends(get_current_user)
):
    return check_url(data["url"])