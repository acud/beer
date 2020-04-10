# this file handles basic building blocks for http requests

from http import client

def get(url, resource):
    conn = client.HTTPSConnection(url)
    conn.request("GET", resource)
    r1 = conn.getresponse()
    data1 = r1.read()
    conn.close()

    return data1, r1.status

