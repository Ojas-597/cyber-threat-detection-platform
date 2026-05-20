from fastapi import APIRouter, Depends
from backend.authentication.dependencies import get_current_user
from backend.incident_response.service import block_ip

router = APIRouter(
    prefix="/response",
    tags=["Incident Response"]
)

@router.post("/block")
def block_suspicious_ip(
    data: dict,
    current_user=Depends(get_current_user)
):
    return block_ip(data["ip"])