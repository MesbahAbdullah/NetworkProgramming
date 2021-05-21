from socket import*

s = socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7000
s.connect((host,port))
while True:
    s.send(input("Client: ").encode("utf-8"))
    if s == 'q':
        break
    x = s.recv(2048)
    print("Server: ", x.decode("utf-8"))
