from fastapi import APIRouter, Depends
from backend.authentication.dependencies import get_current_user
from backend.incident_response.block_ip import block_ip

router = APIRouter(
    prefix="/incident",
    tags=["Incident Response"]
)

@router.post("/block-ip")
def block_suspicious_ip(
    data: dict,
    current_user=Depends(get_current_user)
):
    return block_ip(data["ip"])