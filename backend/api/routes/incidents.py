from fastapi import APIRouter
from backend.database.connection import get_db

router = APIRouter(prefix="/incidents", tags=["Incidents"])

@router.get("/")
def incidents():
    return {"message": "Incident response endpoint"}
