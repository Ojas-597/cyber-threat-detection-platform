def scan_url(url: str):
    suspicious = "login" in url

    return {
        "url": url,
        "phishing": suspicious
    }