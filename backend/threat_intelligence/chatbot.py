"""
Simple cybersecurity
assistant chatbot.
"""


def ask_assistant(
    question: str
):
    """
    Return simple
    security guidance.
    """

    q = question.lower()

    if "ddos" in q:
        return {
            "response":
                "DDoS attacks flood "
                "systems with traffic. "
                "Consider rate limiting "
                "and IP blocking."
        }

    if "phishing" in q:
        return {
            "response":
                "Phishing attacks use "
                "fake domains or "
                "emails. Verify URLs "
                "before clicking."
        }

    if "malware" in q:
        return {
            "response":
                "Malware can infect "
                "systems. Scan files "
                "and isolate endpoints."
        }

    return {
        "response":
            "Threat intelligence "
            "assistant ready."
    }
