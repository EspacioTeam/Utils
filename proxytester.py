from urllib.request import * 
import socket

url="http://ya.ru"

def test(proxy):
    try:
        proxy_handler = ProxyHandler({'http': proxy})
        opener = build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        install_opener(opener)
        req = Request(url)
        sock = urlopen(req)
    except Exception as e:
        print("Error:", e, proxy)
        return False

    return True

def check():
    socket.setdefaulttimeout(1)

    f = open("proxy.lst", 'r')
    g = open("good.lst", 'w')

    for line in f:
        if test(line):
            g.write(line)

    f.close()
    g.close()

check()
