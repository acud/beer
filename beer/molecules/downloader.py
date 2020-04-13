from atoms import request

def downloadFrom(nodeid,namespace, hash):
    url = f"bee-{nodeid}.{namespace}.core.internal:80"
    resource = f"/bzz-chunk/{hash}"
    print(f"downloading from locator {url}{resource}")
    return request.get(url,resource,False)

