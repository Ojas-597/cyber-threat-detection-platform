import hashlib


def create_hash(data):

    return hashlib.sha256(data.encode()).hexdigest()
