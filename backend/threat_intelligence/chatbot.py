from datetime import datetime

# =====================================================
# Cybersecurity Knowledge Base
# =====================================================

responses = {

    "phishing":
        "Phishing attacks steal credentials using fake websites or emails.",

    "ddos":
        "DDoS attacks flood servers with massive traffic.",

    "sql injection":
        "SQL Injection manipulates database queries in vulnerable applications.",

    "ransomware":
        "Ransomware encrypts files and demands payment.",

    "malware":
        "Malware is malicious software designed to damage systems.",

    "xss":
        "Cross-Site Scripting injects malicious scripts into web pages.",

    "mitre":
        "MITRE ATT&CK is a cybersecurity knowledge base of attacker techniques.",

    "cve":
        "CVE stands for Common Vulnerabilities and Exposures."
}

# =====================================================
# AI Chatbot Function
# =====================================================

def chatbot(query):

    query = query.lower()

    for keyword in responses:

        if keyword in query:

            return {

                "query": query,

                "response": responses[keyword],

                "timestamp": str(datetime.now())
            }

    return {

        "query": query,

        "response": "Threat information not available.",

        "timestamp": str(datetime.now())
    }

# =====================================================
# Example Usage
# =====================================================

if __name__ == "__main__":

    question = "What is phishing?"

    print(chatbot(question))
