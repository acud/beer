from molecules import k8s, datagen, uploader, debugger, downloader

def do(size):
    nodes = k8s.nodes()
    data = datagen.generate(size)
    # mock hash
    h = "abcd"

    # do the hashing on data once hasher is implemented in py
    # then uploadto has no side effect of hash - we know what to expect

    uploader.uploadto(0, "elad", data)
    # debugger.waitSync(nodes)
    down = downloader.downloadFrom(0,"elad",h)
    print(down)

    # check that the downloaded hashes content matches what we uploaded
    # compare the hashes but also the bytes




