def check_url(url: str):
    suspicious_words = [
        "login",
        "verify",
        "secure",
        "bank",
        "paypal"
    ]

    for word in suspicious_words:
        if word in url.lower():
            return {
                "url": url,
                "phishing": True,
                "risk": "High"
            }

    return {
        "url": url,
        "phishing": False,
        "risk": "Low"
    }