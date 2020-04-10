from atoms import request, hash, genesis

def getsome():
    hash.sha3("abcd")
    data = genesis.randomBytes(100)
    print(len(data))
    body, status = request.get("swarm-gateways.net", "/")
    print(body, status)

def main():
    getsome()

if __name__ == '__main__':
    main()
