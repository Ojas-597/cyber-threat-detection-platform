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

    # Replace later with password hashing
    if user.password_hash != data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "username": user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
