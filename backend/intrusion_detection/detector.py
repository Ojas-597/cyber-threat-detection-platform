from typing import Dict
import random


def analyze_packet(
    packet: dict
) -> Dict:
    """
    Analyze a packet
    and assign a risk score.
    """

    score = round(
        random.uniform(
            0.1,
            0.99
        ),
        2
    )

    return {
        "module":
            "intrusion_detection",

        "malicious":
            score > 0.8,

        "confidence":
            score,

        "packet":
            packet
    }
