import os
from datetime import datetime, timedelta

from jose import jwt, JWTError

SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "CHANGE_THIS_IN_PRODUCTION"
)

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 2


def create_access_token(data: dict):
    payload = data.copy()

    payload.update(
        {
            "exp":
                datetime.utcnow()
                + timedelta(
                    hours=ACCESS_TOKEN_EXPIRE_HOURS
                )
        }
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None
