from fastapi import APIRouter, Depends
from backend.authentication.dependencies import (
    get_current_user
)
from backend.phishing_detection.service import (
    check_url
)

router = APIRouter(
    prefix="/phishing",
    tags=["Phishing Detection"]
)


@router.post("/check")
def phishing_check(
    data: dict,
    current_user=Depends(
        get_current_user
    )
):
    return check_url(
        data["url"]
    )