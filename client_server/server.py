from socket import*
s = socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7000
s.bind((host,port))
s.listen(5)
while True:
    c,ad = s.accept()
    print("Connection from", ad[0] ,"has been established.")
    x = c.recv(2048)
    print("client: ", x.decode("utf-8"))
    msg = input("Server: ")
    y = c.send(msg.encode("utf-8"))
    if msg == 'q':
        break

c.close()
