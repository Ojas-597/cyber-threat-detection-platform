import re
from urllib.parse import urlparse

# =====================================================
# Suspicious Keywords
# =====================================================

SUSPICIOUS_KEYWORDS = [

    "login",
    "verify",
    "bank",
    "secure",
    "update",
    "account"
]

# =====================================================
# Detect Phishing URL
# =====================================================

def detect_phishing(url):

    score = 0

    parsed = urlparse(url)

    domain = parsed.netloc

    # Long URL

    if len(url) > 75:

        score += 1

    # Suspicious Keywords

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in url.lower():

            score += 1

    # Presence of numbers

    if re.search(r'\\d', domain):

        score += 1

    # Multiple hyphens

    if domain.count("-") >= 2:

        score += 1

    # HTTP instead of HTTPS

    if parsed.scheme == "http":

        score += 1

    # Final Result

    if score >= 3:

        return {

            "url": url,
            "status": "Phishing Detected",
            "risk_score": score
        }

    return {

        "url": url,
        "status": "Safe",
        "risk_score": score
    }

# =====================================================
# Example
# =====================================================

if __name__ == "__main__":

    test_url = "http://secure-bank-login123.com"

    print(detect_phishing(test_url))
