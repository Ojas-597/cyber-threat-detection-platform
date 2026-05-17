from fastapi import APIRouter

router = APIRouter(prefix="/packets", tags=["Packets"])

@router.get("/")
def packets():
    return {"message": "Packet monitoring endpoint"}
backend/authentication/jwt_handler.py
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"


def create_access_token(data: dict):
    payload = data.copy()
    payload.update({"exp": datetime.utcnow() + timedelta(hours=2)})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
