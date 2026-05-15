from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uuid

router = APIRouter(
    prefix="/threats",
    tags=["Threat Management"]
)

# =====================================================
# Threat Data Model
# =====================================================

class Threat(BaseModel):

    type: str
    severity: str
    source_ip: str
    destination_ip: str
    protocol: str
    status: str
    mitre_attack_id: str
    confidence_score: float


# =====================================================
# Dummy Threat Database
# =====================================================

threat_db = [

    {
        "threat_id": str(uuid.uuid4()),
        "type": "DDoS",
        "severity": "Critical",
        "source_ip": "192.168.1.10",
        "destination_ip": "10.0.0.5",
        "protocol": "TCP",
        "status": "Active",
        "mitre_attack_id": "T1498",
        "confidence_score": 98.5,
        "created_at": str(datetime.now())
    },

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
        "created_at": str(datetime.now())
    }
]


# =====================================================
# GET ALL THREATS
# =====================================================

@router.get("/", response_model=List[dict])
def get_all_threats():

    return threat_db


# =====================================================
# GET LIVE THREATS
# =====================================================

@router.get("/live")
def get_live_threats():

    active_threats = [

        threat for threat in threat_db
        if threat["status"] == "Active"
    ]

    return {
        "total_live_threats": len(active_threats),
        "threats": active_threats
    }


# =====================================================
# GET CRITICAL THREATS
# =====================================================

@router.get("/critical")
def get_critical_threats():

    critical = [

        threat for threat in threat_db
        if threat["severity"] == "Critical"
    ]

    return {
        "critical_threats": critical
    }


# =====================================================
# ADD NEW THREAT
# =====================================================

@router.post("/add")
def add_threat(threat: Threat):

    new_threat = {

        "threat_id": str(uuid.uuid4()),
        "type": threat.type,
        "severity": threat.severity,
        "source_ip": threat.source_ip,
        "destination_ip": threat.destination_ip,
        "protocol": threat.protocol,
        "status": threat.status,
        "mitre_attack_id": threat.mitre_attack_id,
        "confidence_score": threat.confidence_score,
        "created_at": str(datetime.now())
    }

    threat_db.append(new_threat)

    return {

        "message": "Threat Added Successfully",
        "threat": new_threat
    }


# =====================================================
# GET THREAT BY ID
# =====================================================

@router.get("/{threat_id}")
def get_threat_by_id(threat_id: str):

    for threat in threat_db:

        if threat["threat_id"] == threat_id:

            return threat

    raise HTTPException(
        status_code=404,
        detail="Threat Not Found"
    )


# =====================================================
# UPDATE THREAT STATUS
# =====================================================

@router.put("/update/{threat_id}")
def update_threat_status(
    threat_id: str,
    status: str
):

    for threat in threat_db:

        if threat["threat_id"] == threat_id:

            threat["status"] = status

            return {

                "message": "Threat Updated Successfully",
                "updated_threat": threat
            }

    raise HTTPException(
        status_code=404,
        detail="Threat Not Found"
    )


# =====================================================
# DELETE THREAT
# =====================================================

@router.delete("/delete/{threat_id}")
def delete_threat(threat_id: str):

    for threat in threat_db:

        if threat["threat_id"] == threat_id:

            threat_db.remove(threat)

            return {

                "message": "Threat Deleted Successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Threat Not Found"
    )


# =====================================================
# THREAT ANALYTICS
# =====================================================

@router.get("/analytics/summary")
def threat_summary():

    total = len(threat_db)

    critical = len([
        t for t in threat_db
        if t["severity"] == "Critical"
    ])

    high = len([
        t for t in threat_db
        if t["severity"] == "High"
    ])

    medium = len([
        t for t in threat_db
        if t["severity"] == "Medium"
    ])

    low = len([
        t for t in threat_db
        if t["severity"] == "Low"
    ])

    return {

        "total_threats": total,
        "critical": critical,
        "high": high,
        "medium": medium,
        "low": low
    }
