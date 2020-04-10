# this file handles everything that has to do with creating bytes
# random or not

import os

def randomBytes(len):
    return os.urandom(len)
