from hashing.hash import create_hash


def verify(original, current):

    return create_hash(original) == current
