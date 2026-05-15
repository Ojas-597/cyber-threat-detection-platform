from pydantic import BaseModel

class Threat(BaseModel):
    attack_type: str
    severity: str
    source_ip: str
    destination_ip: str
