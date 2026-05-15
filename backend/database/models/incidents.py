from pydantic import BaseModel

class Incident(BaseModel):
    action_taken: str
    status: str
    threat_level: str
