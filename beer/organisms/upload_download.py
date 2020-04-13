from molecules import k8s, datagen, uploader, debugger, downloader, hasher

def do(size):
    nodes = k8s.nodes()
    data = datagen.generate(size)

    # mock hash
    h0 = hasher.hashBytes(data)

    print(f"created random bytes. len {size} hash {h0}")

    # do the hashing on data once hasher is implemented in py
    # then uploadto has no side effect of hash - we know what to expect

    print("uploading to node 0")
    uploader.uploadTo(0, "elad", data,h0)

    # does nothing at the moment
    debugger.waitSync(nodes)

    down,code = downloader.downloadFrom(0,"elad",h0)
    if code != 200:
        print("error got status code", code)

    h2 = hasher.hashBytes(down)
    if h0 != h2:
        print("checksum mismatch", h0,h2)

    print("retrieved content hash matches uploaded content")
    print("done for today! thanks!")
