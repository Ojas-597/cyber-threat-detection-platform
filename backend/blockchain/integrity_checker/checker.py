from blockchain.hashing.sha256 import (
    generate_sha256
)


def verify_integrity(
    original_data: str,
    expected_hash: str
):
    """
    Verify integrity.
    """

    current_hash = (
        generate_sha256(
            original_data
        )
    )

    return {
        "valid":
            current_hash
            == expected_hash,
        "current_hash":
            current_hash
    }
