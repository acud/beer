from organisms import upload_download

kib = 1024
mib = 1024*kib
gib = 1024*mib
tib = 1024*gib

def main():
    upload_download.do(3*kib)

if __name__ == '__main__':
    main()
