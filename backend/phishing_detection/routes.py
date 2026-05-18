from fastapi import APIRouter, Depends
from backend.authentication.dependencies import get_current_user
from backend.phishing_detection.service import scan_url

router = APIRouter(
    prefix="/phishing",
    tags=["Phishing Detection"]
)

@router.post("/scan")
def check_url(
    data: dict,
    current_user=Depends(get_current_user)
):
    return scan_url(data["url"])