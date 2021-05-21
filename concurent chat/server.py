from socket import*
from _thread import*
import threading

def receive_thread(c):
    while True:
        x = c.recv(2048)
        print('Client',ad[0],':', x.decode('utf-8'))

def client_thread(c):
    receive = threading.Thread(target=receive_thread, args=(c,))
    receive.start()
    while True:
        c.send(input('Server: ').encode('utf-8'))



s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7000
s.bind((host, port))
s.listen(5)

while True:
    c, ad = s.accept()
    print('Connection from ', ad[0],'has been established.')
    start_new_thread(client_thread, (c,))