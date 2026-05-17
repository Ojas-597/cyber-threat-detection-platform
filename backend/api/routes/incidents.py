from fastapi import APIRouter

router = APIRouter(prefix="/incidents", tags=["Incidents"])

@router.get("/")
def incidents():
    return {"message": "Incident response endpoint"}
