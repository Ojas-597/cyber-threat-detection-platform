import uuid

from backend.database.connection import SessionLocal
from backend.database.models import (
    User,
    Threat,
    Incident,
    Packet,
    BlockchainLog
)

db = SessionLocal()

try:
    # Prevent duplicate admin user
    existing_user = (
        db.query(User)
        .filter(
            User.username == "admin"
        )
        .first()
    )

    if not existing_user:
        admin = User(
            user_id=str(uuid.uuid4()),
            username="admin",
            email="admin@test.com",
            password_hash="admin123"
        )
        db.add(admin)

    # Sample threat
    threat = Threat(
        threat_id=str(uuid.uuid4()),
        type="DDoS",
        severity="Critical",
        source_ip="1.1.1.1",
        destination_ip="10.0.0.1",
        protocol="TCP",
        status="Active",
        mitre_attack_id="T1498",
        confidence_score=95.0
    )
    db.add(threat)

    # Sample incident
    incident = Incident(
        incident_id=str(uuid.uuid4()),
        threat_id=threat.threat_id,
        severity="Critical",
        status="open"
    )
    db.add(incident)

    # Sample packet
    packet = Packet(
        packet_id=str(uuid.uuid4()),
        source_ip="192.168.1.5",
        destination_ip="10.0.0.1",
        protocol="TCP",
        packet_size=512,
        risk_score=75
    )
    db.add(packet)

    # Sample blockchain log
    log = BlockchainLog(
        log_id=str(uuid.uuid4()),
        event_hash="sample_hash_123",
        event_type="ThreatLogged",
        anchored=True,
        blockchain_tx_hash="tx_hash_sample"
    )
    db.add(log)

    db.commit()
    print("Database seeded successfully.")

finally:
    db.close()
