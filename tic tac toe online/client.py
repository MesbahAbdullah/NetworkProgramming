from socket import *
from _thread import *
import threading
import tkinter as tk
from functools import partial

wind = tk.Tk()
wind.geometry('300x400')
playerNumber = 0
message_button = tk.Button(wind, text="Client: O" + str(playerNumber+1), width=15,disabledforeground="black")
message_button.grid(row=0)
message_button["state"] = 'disable'
counter = 0
socket = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7018
socket.connect((host, port))
lastWritten = ''



def createButtons():
    buttons = {} 
    counter=1
    for r in range(1,4):
        for c in range(1,4):
            buttons[f"btn_{counter}"] = tk.Button(wind, text="", width=5,command=partial(clicked, counter), disabledforeground="red")
            buttons[f"btn_{counter}"].grid(row = r+1, column = c)
            counter += 1
    return buttons



def displayRecieved(num):
    bt = btns[f"btn_{num}"]
    bt['text'] = 'X'
    bt['state'] = 'disable'
    global lastWritten
    lastWritten = 'X'
    enableEmptyButtons()
    
    checkEndGame()

def clicked(counter) : 
    btn = btns[f"btn_{counter}"]
    
    btn["text"] = 'O'
    btn["state"] = 'disable'
    socket.send(str(counter).encode("utf-8"))
    print("client" + str(counter) + "send")
    global lastWritten
    lastWritten = 'O'
    checkEndGame()
    disapleAllButtons()

def enableEmptyButtons():
    c = 1
    for i in range(1, 10):
        btn = btns[f"btn_{c}"]
        if btn["text"] == '':
            btn['state'] = 'active'
        c += 1
def disapleAllButtons():
    c = 1
    for i in range(1, 10):
        btn = btns[f"btn_{c}"]
        btn["state"] = 'disable'
        c += 1
def check(btn1, btn2, btn3):
    if(btn1["text"] == btn2["text"] == btn3["text"] != ''):
        return True
    else:
        return False
def checkEndGame():
    global playerNumber
    global button
    global counter
    if(check(btns["btn_1"], btns["btn_2"], btns["btn_3"]) or check(btns["btn_4"], btns["btn_5"], btns["btn_6"]) or\
        check(btns["btn_7"], btns["btn_8"], btns["btn_9"]) or check(btns["btn_1"], btns["btn_4"], btns["btn_7"]) or\
        check(btns["btn_2"], btns["btn_5"], btns["btn_8"]) or check(btns["btn_3"], btns["btn_6"], btns["btn_9"]) or\
        check(btns["btn_1"], btns["btn_5"], btns["btn_9"]) or check(btns["btn_7"], btns["btn_5"], btns["btn_3"])):
        message_button['text'] = "Player " + lastWritten + " wins."
        disapleAllButtons()
    elif counter == 8:
        message_button['text'] = "No player wins."
    counter += 1

btns = createButtons()


def recieved_thread(c):
    while True:
        x=c.recv(500)
        displayRecieved(int(x.decode("utf-8")))
start_new_thread(recieved_thread, (socket,))
tk.mainloop()
