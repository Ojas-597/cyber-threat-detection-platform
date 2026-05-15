import requests
from datetime import datetime

# =====================================================
# NVD CVE API URL
# =====================================================

NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# =====================================================
# Fetch Latest CVEs
# =====================================================

def fetch_latest_cves():

    try:

        response = requests.get(NVD_API_URL)

        data = response.json()

        vulnerabilities = []

        for item in data.get("vulnerabilities", [])[:10]:

            cve = item.get("cve", {})

            vulnerabilities.append({

                "cve_id": cve.get("id"),

                "published": cve.get("published"),

                "last_modified": cve.get("lastModified"),

                "description": cve.get(
                    "descriptions",
                    [{}]
                )[0].get("value")
            })

        return {

            "status": "success",

            "total_records": len(vulnerabilities),

            "timestamp": str(datetime.now()),

            "cves": vulnerabilities
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

    result = fetch_latest_cves()

    print(result)
