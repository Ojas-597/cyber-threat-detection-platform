from pydantic import BaseModel

class BlockchainLog(BaseModel):
    previous_hash: str
    current_hash: str
    event_data: dict
