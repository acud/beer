# this file handles hashing
import hashlib

def sha3(content):
    s = hashlib.sha3_512()
    s.update(content)
    # s.update(content.encode('utf-8'))
    return s.hexdigest()

