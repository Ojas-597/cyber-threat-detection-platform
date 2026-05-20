import os

from fastapi import Depends, HTTPException
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from jose import jwt, JWTError

security = HTTPBearer()

SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "CHANGE_THIS_IN_PRODUCTION"
)

ALGORITHM = "HS256"


def get_current_user(
    credentials:
    HTTPAuthorizationCredentials
    = Depends(security)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )