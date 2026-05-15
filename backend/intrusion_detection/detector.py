import random

attack_types = [

    "Normal",
    "DDoS",
    "SQL Injection",
    "Port Scanning",
    "Brute Force",
    "Phishing"
]

def detect_attack(packet):

    prediction = random.choice(attack_types)

    return {
        "packet": packet,
        "prediction": prediction
    }
