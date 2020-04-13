from atoms import hash as hashing

def hashBytes(data):
    return hashing.sha3(data)
