from fastapi import APIRouter, Depends
from backend.authentication.dependencies import get_current_user
from backend.blockchain.service import log_event

router = APIRouter(
    prefix="/blockchain",
    tags=["Blockchain"]
)

@router.post("/log")
def add_log(
    data: dict,
    current_user=Depends(get_current_user)
):
    return log_event(data["event"])