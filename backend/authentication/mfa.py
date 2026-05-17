import os
import secrets
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from typing import Dict, Optional

# In-memory OTP store (replace with Redis/DB in production)
otp_store: Dict[str, dict] = {}

# OTP settings
OTP_EXPIRY_MINUTES = 5


def generate_otp(length: int = 6) -> str:
    """
    Generate a secure numeric OTP.
    """
    digits = "0123456789"
    return "".join(
        secrets.choice(digits)
        for _ in range(length)
    )


def store_otp(
    username: str,
    otp: str
) -> None:
    """
    Store OTP temporarily with expiry.
    """
    otp_store[username] = {
        "otp": otp,
        "expires_at": datetime.utcnow()
        + timedelta(minutes=OTP_EXPIRY_MINUTES)
    }


def verify_otp(
    username: str,
    otp: str
) -> bool:
    """
    Verify OTP and delete after successful use.
    """
    record: Optional[dict] = otp_store.get(username)

    if not record:
        return False

    if datetime.utcnow() > record["expires_at"]:
        otp_store.pop(username, None)
        return False

    if record["otp"] != otp:
        return False

    # OTP should be single-use
    otp_store.pop(username, None)
    return True


def send_otp_email(
    receiver_email: str,
    otp: str
) -> dict:
    """
    Send OTP email using SMTP.

    Required environment variables:
    EMAIL_ADDRESS
    EMAIL_PASSWORD
    """

    sender_email = os.getenv(
        "EMAIL_ADDRESS"
    )
    sender_password = os.getenv(
        "EMAIL_PASSWORD"
    )

    if not sender_email or not sender_password:
        return {
            "success": False,
            "error": (
                "Email credentials not "
                "configured"
            )
        }

    subject = (
        "Cyber Threat Detection "
        "Platform MFA OTP"
    )

    body = f"""
Your One-Time Password (OTP) is:

{otp}

This OTP expires in
{OTP_EXPIRY_MINUTES} minutes.

Do not share this code
with anyone.
"""

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as server:
            server.starttls()
            server.login(
                sender_email,
                sender_password
            )

            server.sendmail(
                sender_email,
                receiver_email,
                message.as_string()
            )

        return {
            "success": True,
            "message": (
                "OTP sent successfully"
            )
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
