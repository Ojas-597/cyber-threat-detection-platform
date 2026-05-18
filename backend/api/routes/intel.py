from fastapi import (
    APIRouter,
    Depends
)

from backend.authentication.dependencies import (
    get_current_user
)

from backend.threat_intelligence.service import (
    lookup_ip
)

router = APIRouter(
    prefix="/intel",
    tags=["Threat Intelligence"]
)


@router.post("/ip")
def check_ip(
    data: dict,
    current_user=Depends(
        get_current_user
    )
):
    return lookup_ip(
        data["ip"]
    )
