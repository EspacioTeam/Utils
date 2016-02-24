import socket
import sys
import os
import time

HOST = '188.166.133.53'
PORT = 11491
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    time.sleep(1)
    data = s.recv(1024)
    print(data)
    data = data.decode("utf-8").split('\n')[1]
    data = data[data.find(':')+2:]

    print(data)
    f = open('input', 'w+')
    print(f.write(data))
    f.close()
    # os.remove('output')
    os.system('./test')

    f = open('output', 'rb')
    ans = f.read()
    f.close()
    print('Answer:', ans)
    s.sendall(ans)

# s.sendall('Hello, world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)
