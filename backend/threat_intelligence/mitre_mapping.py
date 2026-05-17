"""
MITRE ATT&CK technique mapping
for detected threats.
"""

MITRE_MAP = {
    "DDoS": {
        "technique_id": "T1498",
        "name": "Network Denial of Service"
    },
    "SQL Injection": {
        "technique_id": "T1190",
        "name": "Exploit Public-Facing Application"
    },
    "Phishing": {
        "technique_id": "T1566",
        "name": "Phishing"
    },
    "Malware": {
        "technique_id": "T1204",
        "name": "User Execution"
    }
}


def get_mitre_mapping(
    threat_type: str
):
    """
    Return MITRE ATT&CK mapping
    for a threat type.
    """

    return MITRE_MAP.get(
        threat_type,
        {
            "technique_id":
                "Unknown",
            "name":
                "Unknown Technique"
        }
    )
