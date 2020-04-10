# this file handles hashing
import hashlib

def sha3(content):
    s = hashlib.sha3_512()
    print(s.name)
    print(s.digest_size)

    s.update(content.encode('utf-8'))
    print(s.hexdigest())

