import requests
from datetime import datetime

# =====================================================
# VirusTotal API Configuration
# =====================================================

API_KEY = "YOUR_VIRUSTOTAL_API_KEY"

BASE_URL = "https://www.virustotal.com/api/v3/urls"

HEADERS = {
    "x-apikey": API_KEY
}

# =====================================================
# Submit URL For Analysis
# =====================================================

def analyze_url(url):

    payload = {
        "url": url
    }

    try:

        response = requests.post(
            BASE_URL,
            headers=HEADERS,
            data=payload
        )

        return {

            "status": "submitted",
            "response": response.json(),
            "timestamp": str(datetime.now())
        }

    except Exception as e:

        return {

            "status": "error",
            "message": str(e)
        }

# =====================================================
# Get Analysis Report
# =====================================================

def get_analysis(analysis_id):

    endpoint = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

    try:

        response = requests.get(
            endpoint,
            headers=HEADERS
        )

        data = response.json()

        return {

            "analysis_result": data,
            "timestamp": str(datetime.now())
        }

    except Exception as e:

        return {

            "status": "error",
            "message": str(e)
        }

# =====================================================
# Example Usage
# =====================================================

if __name__ == "__main__":

    sample_url = "http://malicious-example.com"

    result = analyze_url(sample_url)

    print(result)
