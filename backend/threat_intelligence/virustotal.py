"""
VirusTotal integration
(mock implementation).
"""

KNOWN_MALICIOUS_HASHES = {
    "e3b0c44298fc1c149afbf4c8996fb924":
        True
}


def check_hash(
    file_hash: str
):
    """
    Check file hash
    against known malicious list.
    """

    malicious = (
        file_hash
        in KNOWN_MALICIOUS_HASHES
    )

    return {
        "source":
            "VirusTotal",
        "hash":
            file_hash,
        "malicious":
            malicious
    }
