from socket import *
from _thread import *
import threading

def receive_thread(s):
    while True:
        x = s.recv(2048)
        print('Server: ', x.decode('utf-8'))


s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7000
s.connect((host, port))

receive = threading.Thread(target=receive_thread, args=(s, ))
receive.start()

while True:
    s.send(input('Client: ').encode('utf-8'))
