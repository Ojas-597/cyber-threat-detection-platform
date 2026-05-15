import os
from datetime import datetime

# =====================================================
# Block IP Address
# =====================================================

def block_ip(ip_address):

    command = f"netsh advfirewall firewall add rule name=Block_{ip_address} dir=in action=block remoteip={ip_address}"

    try:

        os.system(command)

        return {

            "status": "success",
            "blocked_ip": ip_address,
            "timestamp": str(datetime.now())
        }

    except Exception as e:

        return {

            "status": "failed",
            "error": str(e)
        }

# =====================================================
# Unblock IP Address
# =====================================================

def unblock_ip(ip_address):

    command = f"netsh advfirewall firewall delete rule name=Block_{ip_address}"

    try:

        os.system(command)

        return {

            "status": "unblocked",
            "ip": ip_address
        }

    except Exception as e:

        return {

            "status": "failed",
            "error": str(e)
        }

# =====================================================
# Example
# =====================================================

if __name__ == "__main__":

    print(block_ip("192.168.1.100"))
