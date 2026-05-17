import random
from datetime import (
    datetime,
    timedelta
)

# Temporary OTP store
# Replace with Redis/DB later
otp_store = {}

OTP_EXPIRY_MINUTES = 5


def generate_otp(
    username: str
):
    """
    Generate 6-digit MFA OTP
    for a user.
    """

    otp = str(
        random.randint(
            100000,
            999999
        )
    )

    expiry = (
        datetime.utcnow()
        + timedelta(
            minutes=
            OTP_EXPIRY_MINUTES
        )
    )

    otp_store[
        username
    ] = {
        "otp":
            otp,
        "expires_at":
            expiry
    }

    return {
        "username":
            username,
        "otp":
            otp,
        "expires_at":
            expiry.isoformat()
    }


def verify_otp(
    username: str,
    otp: str
):
    """
    Verify MFA OTP.
    """

    record = (
        otp_store.get(
            username
        )
    )

    if not record:
        return {
            "success":
                False,
            "message":
                "No OTP found"
        }

    if (
        datetime.utcnow()
        > record[
            "expires_at"
        ]
    ):
        del otp_store[
            username
        ]

        return {
            "success":
                False,
            "message":
                "OTP expired"
        }

    if (
        record["otp"]
        != otp
    ):
        return {
            "success":
                False,
            "message":
                "Invalid OTP"
        }

    del otp_store[
        username
    ]

    return {
        "success":
            True,
        "message":
            "OTP verified"
    }
