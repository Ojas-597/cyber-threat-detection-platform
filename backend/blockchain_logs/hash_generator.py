import hashlib
from datetime import datetime

# =====================================================
# Generate SHA256 Hash
# =====================================================

def generate_hash(data):

    encoded = data.encode()

    hashed = hashlib.sha256(encoded)

    return hashed.hexdigest()

# =====================================================
# Create Blockchain Log
# =====================================================

def create_block(event_data, previous_hash):

    timestamp = str(datetime.now())

    block_data = f"{event_data}{timestamp}{previous_hash}"

    current_hash = generate_hash(block_data)

    block = {

        "timestamp": timestamp,
        "event_data": event_data,
        "previous_hash": previous_hash,
        "current_hash": current_hash
    }

    return block

# =====================================================
# Example
# =====================================================

if __name__ == "__main__":

    block = create_block(

        event_data="Threat Detected",
        previous_hash="0000000000"
    )

    print(block)
