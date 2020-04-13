from atoms import request

def downloadFrom(nodeid,namespace, hash):
    url = f"bee-{nodeid}.{namespace}.core.internal:80"
    resource = f"/bzz-chunk/{hash}"
    return request.get(url,resource,False)

