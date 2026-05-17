import ipaddress
from datetime import datetime

# In-memory blocked IP registry
# Replace with database storage later
blocked_ips = []


def block_ip(ip_address: str) -> dict:
    """
    Validate and simulate blocking
    a malicious IP address.
    """

    try:
        # Validate IP format
        ipaddress.ip_address(
            ip_address
        )

    except ValueError:
        return {
            "success": False,
            "message": "Invalid IP address"
        }

    # Prevent duplicates
    existing = next(
        (
            entry
            for entry in blocked_ips
            if entry["ip_address"]
            == ip_address
        ),
        None
    )

    if existing:
        return {
            "success": True,
            "message":
                "IP already blocked",
            "blocked_ip":
                existing
        }

    blocked_entry = {
        "ip_address":
            ip_address,
        "blocked_at":
            datetime.utcnow()
            .isoformat(),
        "status":
            "blocked"
    }

    blocked_ips.append(
        blocked_entry
    )

    return {
        "success": True,
        "message":
            "IP blocked successfully",
        "blocked_ip":
            blocked_entry
    }


def get_blocked_ips():
    """
    Return all blocked IPs.
    """
    return blocked_ips


def unblock_ip(
    ip_address: str
) -> dict:
    """
    Remove IP from blocked list.
    """

    for entry in blocked_ips:
        if (
            entry["ip_address"]
            == ip_address
        ):
            blocked_ips.remove(
                entry
            )

            return {
                "success": True,
                "message":
                    "IP unblocked"
            }

    return {
        "success": False,
        "message":
            "IP not found"
    }
