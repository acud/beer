from atoms import request

def uploadTo(nodeid, namespace, data,h):
    url = f"bee-{nodeid}.{namespace}.core.internal:80"
    resource = f"/bzz-chunk/{h}"
    print(f"uploading to locator: {url}{resource}")
    return request.post(url,resource,False,data)

