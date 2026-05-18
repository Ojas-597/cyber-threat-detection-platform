from fastapi import APIRouter, Depends
from backend.authentication.dependencies import (
    get_current_user
)
from backend.incident_response.block_ip import (
    block_ip
)

router = APIRouter(
    prefix="/response",
    tags=["Incident Response"]
)


@router.post("/block-ip")
def response_block(
    data: dict,
    current_user=Depends(
        get_current_user
    )
):
    return block_ip(
        data["ip"]
    )