from pydantic import BaseModel

class Packet(BaseModel):
    source_ip: str
    destination_ip: str
    protocol: str
    packet_size: int
