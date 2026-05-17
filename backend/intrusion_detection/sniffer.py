import random
import uuid
from datetime import datetime


PROTOCOLS = [
    "TCP",
    "UDP",
    "HTTP",
    "HTTPS",
    "ICMP"
]


def capture_packet():
    """
    Simulate capturing
    a network packet.
    """

    source_ip = (
        f"192.168.1."
        f"{random.randint(1, 254)}"
    )

    destination_ip = (
        f"10.0.0."
        f"{random.randint(1, 254)}"
    )

    packet = {
        "packet_id":
            str(uuid.uuid4()),
        "source_ip":
            source_ip,
        "destination_ip":
            destination_ip,
        "protocol":
            random.choice(
                PROTOCOLS
            ),
        "packet_size":
            random.randint(
                64,
                1500
            ),
        "captured_at":
            datetime.utcnow()
            .isoformat()
    }

    return packet


def capture_multiple(
    count: int = 5
):
    """
    Capture multiple
    simulated packets.
    """

    packets = []

    for _ in range(count):
        packets.append(
            capture_packet()
        )

    return packets
