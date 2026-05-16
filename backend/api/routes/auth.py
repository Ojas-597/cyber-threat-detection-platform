from fastapi import APIRouter
from pydantic import BaseModel
from authentication.jwt_handler import create_access_token

router = APIRouter(prefix="/auth",
                  tags=["Authentication"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):

    token = create_access_token({
        "username": data.username
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
