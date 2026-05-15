from datetime import datetime

# =====================================================
# MITRE ATT&CK Technique Mapping
# =====================================================

mitre_mapping = {

    "Phishing": {

        "technique_id": "T1566",

        "technique_name": "Phishing",

        "tactic": "Initial Access",

        "description": "Adversaries send phishing emails to steal credentials.",

        "severity": "High"
    },

    "SQL Injection": {

        "technique_id": "T1190",

        "technique_name": "Exploit Public-Facing Application",

        "tactic": "Initial Access",

        "description": "Attackers exploit vulnerable web applications using SQL queries.",

        "severity": "Critical"
    },

    "DDoS": {

        "technique_id": "T1498",

        "technique_name": "Network Denial of Service",

        "tactic": "Impact",

        "description": "Flooding servers with excessive traffic.",

        "severity": "Critical"
    },

    "Port Scanning": {

        "technique_id": "T1046",

        "technique_name": "Network Service Scanning",

        "tactic": "Discovery",

        "description": "Scanning open ports and services.",

        "severity": "Medium"
    },

    "Brute Force": {

        "technique_id": "T1110",

        "technique_name": "Brute Force",

        "tactic": "Credential Access",

        "description": "Repeated login attempts using password guessing.",

        "severity": "High"
    },

    "Ransomware": {

        "technique_id": "T1486",

        "technique_name": "Data Encrypted for Impact",

        "tactic": "Impact",

        "description": "Encrypting victim data for ransom.",

        "severity": "Critical"
    },

    "Malware": {

        "technique_id": "T1204",

        "technique_name": "User Execution",

        "tactic": "Execution",

        "description": "Malicious software execution on target systems.",

        "severity": "High"
    },

    "Credential Theft": {

        "technique_id": "T1003",

        "technique_name": "OS Credential Dumping",

        "tactic": "Credential Access",

        "description": "Stealing stored credentials from operating systems.",

        "severity": "Critical"
    },

    "Cross Site Scripting": {

        "technique_id": "T1059",

        "technique_name": "Command and Scripting Interpreter",

        "tactic": "Execution",

        "description": "Injecting malicious scripts into web applications.",

        "severity": "High"
    },

    "Man-in-the-Middle": {

        "technique_id": "T1557",

        "technique_name": "Adversary-in-the-Middle",

        "tactic": "Collection",

        "description": "Intercepting network communications.",

        "severity": "High"
    }
}

# =====================================================
# Get MITRE Mapping By Threat Name
# =====================================================

def get_mitre_mapping(threat_name):

    threat = mitre_mapping.get(threat_name)

    if threat:

        return {

            "threat": threat_name,

            "mapping": threat,

            "timestamp": str(datetime.now())
        }

    return {

        "error": "Threat Not Found in MITRE ATT&CK Database"
    }

# =====================================================
# Get All MITRE Techniques
# =====================================================

def get_all_mappings():

    return {

        "total_techniques": len(mitre_mapping),

        "mappings": mitre_mapping
    }

# =====================================================
# Example Usage
# =====================================================

if __name__ == "__main__":

    result = get_mitre_mapping("Ransomware")

    print(result)
