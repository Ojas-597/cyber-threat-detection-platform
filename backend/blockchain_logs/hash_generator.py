import hashlib
import json
from typing import Any


def generate_hash(
    data: Any
) -> str:
    """
    Generate deterministic SHA-256 hash
    from any serializable data.

    Used for:
    - Threat log anchoring
    - Integrity verification
    - Blockchain audit trail
    """

    try:
        normalized = json.dumps(
            data,
            sort_keys=True,
            separators=(
                ",",
                ":"
            ),
            default=str
        )

        sha256_hash = (
            hashlib.sha256(
                normalized.encode(
                    "utf-8"
                )
            ).hexdigest()
        )

        return sha256_hash

    except Exception as e:
        raise ValueError(
            f"Hash generation failed: "
            f"{str(e)}"
        )


def verify_hash(
    data: Any,
    expected_hash: str
) -> bool:
    """
    Verify that generated hash
    matches expected hash.
    """

    generated_hash = (
        generate_hash(
            data
        )
    )

    return (
        generated_hash
        == expected_hash
    )
