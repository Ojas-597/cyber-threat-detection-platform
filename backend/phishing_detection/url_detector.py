import re
from typing import Dict


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank"
]


def detect_phishing(
    url: str
) -> Dict:
    """
    Basic phishing URL detector.
    """

    url_lower = url.lower()

    suspicious = any(
        keyword in url_lower
        for keyword in SUSPICIOUS_KEYWORDS
    )

    has_ip_address = bool(
        re.search(
            r"(?:\d{1,3}\.){3}\d{1,3}",
            url
        )
    )

    risk_score = 0.2

    if suspicious:
        risk_score += 0.4

    if has_ip_address:
        risk_score += 0.4

    return {
        "module":
            "phishing_detection",
        "url":
            url,
        "phishing":
            risk_score >= 0.7,
        "confidence":
            round(risk_score, 2)
    }
