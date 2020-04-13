# this file handles basic building blocks for http requests

from http import client

def get(url, resource, https):
    return doReq(url, resource, "", https, "GET")

def post(url,resource, https, body):
    return doReq(url, resource, body, https, "POST")

def put(url,resource, https, body):
    return doReq(url, resource, body, https, "PUT")

def delete(url,resource, https, body):
    return doReq(url, resource, "", https, "DELETE")


def doReq(url, resource, body, https, method):
    conn = None
    if https == True:
        conn = client.HTTPSConnection(url)
    else:
        conn = client.HTTPConnection(url)

    conn.request(method, resource)
    resp = conn.getresponse()
    data = resp.read()
    conn.close()
    return data, resp.status
