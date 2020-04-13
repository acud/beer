from atoms import request

def uploadto(nodeid, namespace, data):
    url = f"bee-{nodeid}.{namespace}.core.internal:80"
    print(url)
    return request.post(url,"/bzz-chunk/abcd",False,data)

