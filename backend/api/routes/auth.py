from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.authentication.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    if data.username != "admin" or data.password != "admin123":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"username": data.username})
    return {"access_token": token, "token_type": "bearer"}
backend/api/routes/threats.py
from fastapi import APIRouter

router = APIRouter(prefix="/threats", tags=["Threats"])

@router.get("/live")
def get_live_threats():
    return {
        "total_live_threats": 3,
        "threats": []
    }

@router.get("/analytics/summary")
def summary():
    return {
        "critical": 1,
        "high": 1,
        "medium": 1,
        "low": 0
    }
