import hashlib


def generate_sha256(
    data: str
) -> str:
    """
    Generate SHA256 hash.
    """

    return hashlib.sha256(
        data.encode()
    ).hexdigest()
