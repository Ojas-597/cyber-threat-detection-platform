def detect_intrusion(ip: str):
    suspicious_ips = [
        "192.168.1.100",
        "10.0.0.5"
    ]

    if ip in suspicious_ips:
        return {
            "ip": ip,
            "intrusion": True,
            "severity": "High"
        }

    return {
        "ip": ip,
        "intrusion": False,
        "severity": "Low"
    }