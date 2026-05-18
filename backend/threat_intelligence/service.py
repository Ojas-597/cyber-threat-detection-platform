def lookup_ip(ip: str):
    malicious_ips = [
        "8.8.8.8",
        "1.2.3.4"
    ]

    if ip in malicious_ips:
        return {
            "ip": ip,
            "malicious": True,
            "reputation":
                "Bad"
        }

    return {
        "ip": ip,
        "malicious": False,
        "reputation":
            "Good"
    }
