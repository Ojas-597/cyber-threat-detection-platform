from datetime import datetime

from backend.blockchain_logs.hash_generator import (
    generate_hash
)


def log_event(
    event: dict
):
    event_hash = (
        generate_hash(
            event
        )
    )

    return {
        "timestamp":
            datetime.utcnow()
            .isoformat(),
        "event":
            event,
        "event_hash":
            event_hash,
        "anchored":
            True,
    }
