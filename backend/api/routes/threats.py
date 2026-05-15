from fastapi import APIRouter

router = APIRouter(prefix="/threats")

@router.get("/live")
def live_threats():

    return {
        "threats": [
            {
                "type": "DDoS",
                "severity": "Critical"
            }
        ]
    }
