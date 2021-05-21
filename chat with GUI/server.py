from socket import*
import threading
from _thread import *
from tkinter import *

window = Tk()
window.geometry('300x400')
window.title("Server")
en = Entry(window, width=30)
en.grid(column=1, row=1)
lbl = Label(window)
lbl.grid(column=2, row=8)

def clicked():
    msg = en.get()
    lbl["text"] +="Me: "+ msg + '\n'
    c.send(msg.encode("utf_8"))
    en.delete(0,END) 


bt = Button(window, width=10, height=2, text="send", command=clicked)
bt.grid(column=2, row=2)

def rcvThread(c):
    while True:
         x = c.recv(2048).decode("utf_8")
         lbl["text"] +="client: "+ x + '\n'
        

def clientThread(c):
    receive = threading.Thread(target=rcvThread, args=(c,))
    receive.start()
    

s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7000
s.bind((host, port))
s.listen(5)
c, ad = s.accept()

start_new_thread(clientThread, (c,))

window.mainloop()
c.close()