from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.authentication.jwt_handler import (
    create_access_token
)
from backend.authentication.mfa import (
    generate_otp,
    verify_otp
)
from backend.database.connection import (
    get_db
)
from backend.database.models.users import (
    User
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


class LoginRequest(BaseModel):
    username: str
    password: str


class OTPVerifyRequest(BaseModel):
    username: str
    otp: str


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(
            User.username == data.username
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if user.password_hash != data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="User account disabled"
        )

    # MFA enabled
    if user.mfa_enabled:
        otp_data = generate_otp(
            user.username
        )

        return {
            "message":
                "MFA required",
            "mfa_required":
                True,
            "otp":
                otp_data["otp"]
        }

    # Normal login
    token = create_access_token(
        {
            "username":
                user.username
        }
    )

    return {
        "access_token":
            token,
        "token_type":
            "bearer",
        "mfa_required":
            False
    }


@router.post("/verify-otp")
def verify_mfa(
    data: OTPVerifyRequest,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(
            User.username == data.username
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    result = verify_otp(
        data.username,
        data.otp
    )

    if not result["success"]:
        raise HTTPException(
            status_code=401,
            detail=result["message"]
        )

    token = create_access_token(
        {
            "username":
                user.username
        }
    )

    return {
        "access_token":
            token,
        "token_type":
            "bearer"
    }
