from atoms import request

def getsome():
    body, status = request.get("swarm-gateways.net")
    print(body, status)

def main():
    getsome()

if __name__ == '__main__':
    main()
