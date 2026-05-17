from datetime import datetime
from enum import Enum
from typing import List
import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.incident_response.service import (
    create_incident
)
from backend.blockchain_logs.logger import (
    log_event
)
from backend.threat_intelligence.feeds import (
    get_iocs
)

router = APIRouter(
    prefix="/threats",
    tags=["Threat Management"]
)

# ==========================================
# ENUMS
# ==========================================


class Severity(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Status(str, Enum):
    ACTIVE = "Active"
    BLOCKED = "Blocked"
    RESOLVED = "Resolved"


class Protocol(str, Enum):
    TCP = "TCP"
    UDP = "UDP"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    ICMP = "ICMP"


# ==========================================
# DATA MODELS
# ==========================================


class Threat(BaseModel):
    type: str = Field(
        ...,
        min_length=2,
        max_length=100
    )
    severity: Severity
    source_ip: str
    destination_ip: str
    protocol: Protocol
    status: Status
    mitre_attack_id: str
    confidence_score: float = Field(
        ...,
        ge=0,
        le=100
    )


class ThreatResponse(Threat):
    threat_id: str
    created_at: str
    incident: dict | None = None
    blockchain_log: dict | None = None
    intel_match: bool = False


class ThreatStatusUpdate(BaseModel):
    status: Status


# ==========================================
# IN-MEMORY DATABASE
# Replace with PostgreSQL later
# ==========================================

threat_db = []

# Seed data
threat_db.append(
    {
        "threat_id": str(uuid.uuid4()),
        "type": "DDoS",
        "severity": "Critical",
        "source_ip": "185.220.101.1",
        "destination_ip": "10.0.0.5",
        "protocol": "TCP",
        "status": "Active",
        "mitre_attack_id": "T1498",
        "confidence_score": 98.5,
        "created_at": str(
            datetime.utcnow()
        ),
    }
)

threat_db.append(
    {
        "threat_id": str(uuid.uuid4()),
        "type": "SQL Injection",
        "severity": "High",
        "source_ip": "172.16.0.25",
        "destination_ip": "10.0.0.15",
        "protocol": "HTTP",
        "status": "Blocked",
        "mitre_attack_id": "T1190",
        "confidence_score": 92.7,
        "created_at": str(
            datetime.utcnow()
        ),
    }
)


# ==========================================
# GET ALL THREATS
# ==========================================


@router.get(
    "/",
    response_model=List[
        ThreatResponse
    ]
)
def get_all_threats():
    return threat_db


# ==========================================
# GET LIVE THREATS
# Used by frontend dashboard
# ==========================================


@router.get("/live")
def get_live_threats():
    active = [
        t
        for t in threat_db
        if t["status"] == "Active"
    ]

    return {
        "total_live_threats":
            len(active),
        "threats":
            active
    }


# ==========================================
# THREAT ANALYTICS
# Used by frontend dashboard
# ==========================================


@router.get(
    "/analytics/summary"
)
def threat_summary():
    return {
        "total_threats":
            len(threat_db),
        "critical":
            len([
                t for t in threat_db
                if t["severity"]
                == "Critical"
            ]),
        "high":
            len([
                t for t in threat_db
                if t["severity"]
                == "High"
            ]),
        "medium":
            len([
                t for t in threat_db
                if t["severity"]
                == "Medium"
            ]),
        "low":
            len([
                t for t in threat_db
                if t["severity"]
                == "Low"
            ]),
    }


# ==========================================
# GET THREAT BY ID
# ==========================================


@router.get(
    "/id/{threat_id}",
    response_model=
    ThreatResponse
)
def get_threat_by_id(
    threat_id: str
):
    for threat in threat_db:
        if (
            threat["threat_id"]
            == threat_id
        ):
            return threat

    raise HTTPException(
        status_code=404,
        detail="Threat not found"
    )


# ==========================================
# ADD NEW THREAT
# Auto:
# - checks threat intel
# - creates incident
# - logs blockchain event
# ==========================================


@router.post(
    "/add",
    response_model=
    ThreatResponse
)
def add_threat(
    threat: Threat
):
    intel = get_iocs()

    intel_match = (
        threat.source_ip
        in intel[
            "malicious_ips"
        ]
    )

    incident = None

    if (
        threat.severity
        == Severity.CRITICAL
    ):
        incident = (
            create_incident(
                str(uuid.uuid4()),
                threat.severity
            )
        )

    blockchain_event = (
        log_event(
            {
                "type":
                    threat.type,
                "source_ip":
                    threat.source_ip,
            }
        )
    )

    new_threat = {
        "threat_id":
            str(uuid.uuid4()),
        "created_at":
            str(
                datetime.utcnow()
            ),
        **threat.dict(),
        "incident":
            incident,
        "blockchain_log":
            blockchain_event,
        "intel_match":
            intel_match,
    }

    threat_db.append(
        new_threat
    )

    return new_threat


# ==========================================
# UPDATE STATUS
# ==========================================


@router.put(
    "/update/{threat_id}"
)
def update_status(
    threat_id: str,
    update:
    ThreatStatusUpdate
):
    for threat in threat_db:
        if (
            threat["threat_id"]
            == threat_id
        ):
            threat[
                "status"
            ] = (
                update.status
            )

            return {
                "message":
                    "Threat updated",
                "threat":
                    threat,
            }

    raise HTTPException(
        status_code=404,
        detail="Threat not found"
    )


# ==========================================
# DELETE THREAT
# ==========================================


@router.delete(
    "/delete/{threat_id}"
)
def delete_threat(
    threat_id: str
):
    for threat in threat_db:
        if (
            threat["threat_id"]
            == threat_id
        ):
            threat_db.remove(
                threat
            )

            return {
                "message":
                    "Threat deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="Threat not found"
    )
