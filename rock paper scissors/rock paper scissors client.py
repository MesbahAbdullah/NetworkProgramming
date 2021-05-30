from tkinter import *
from PIL import Image, ImageTk
from socket import*
import threading
from _thread import *

win = Tk()
win.title("Tic Tac Toe client side")
win.configure(bg="black")
win.geometry("650x550")

result=StringVar()
yourScore=IntVar()
otherPlayerScore=IntVar()
################## socket initialization ##################
s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7060
s.connect((host, port))


#################### Receiving part #########################
receiveFlag=0
sentFlag=0
recievedNum=0
sentNum=0
def rcvThread(c):
    while True:
      global recievedNum
      recievedNum = c.recv(518).decode("utf_8")
      global receiveFlag
      receiveFlag=1    
      checkWinner(int(sentNum),int(recievedNum))
      enableAllButtons()   
      
receive = threading.Thread(target=rcvThread, args=(s,))
receive.start()

######################## FUNCTIONS #######################
def draw():
  out="                     It's a Draw"
  result.set(out)

def youWon():
  out = "                     You Won"
  result.set(out)
  otherPlayerScore.set(otherPlayerScore.get() +1)

def otherPlayerWon():
  out = "                     You Lost"
  result.set(out)
  yourScore.set(yourScore.get() + 1)

def disapleAllButtons():
  button1["state"] = 'disable'
  button2["state"] = 'disable'
  button3["state"] = 'disable'


def enableAllButtons():
  button1["state"] = 'active'
  button2["state"] = 'active'
  button3["state"] = 'active'

def userChoice(num):       #will send number one to client to represent sotone 
  disapleAllButtons()
  global sentNum
  sentNum=num  
  s.send(str(num).encode("utf_8"))
  global sentFlag
  sentFlag=1
  global recievedNum
  checkWinner(int(sentNum),int(recievedNum))
  
     

def checkWinner(sentNum,recievedNum):   #1-->stone , 2-->paper  ,3-->scissors
  global sentFlag
  global receiveFlag
  if sentFlag==1 and receiveFlag==1:
      sentFlag=0  
      receiveFlag=0
      if sentNum==recievedNum:
        draw()
      elif((sentNum==1 and recievedNum==3) or (sentNum==2 and recievedNum==1) or (sentNum==3 and recievedNum==2)):
         youWon()
      elif((recievedNum==1 and sentNum==3) or (recievedNum==2 and sentNum==1) or (recievedNum==3 and sentNum==2)):
          otherPlayerWon()
  
  
  

 
    
# ------------------------IMAGE DATA----------------------

stone_image1 = Image.open("G:\\F_Y_S_S\\network\lap\\rock\\Rock.png")
stone_image = ImageTk.PhotoImage(stone_image1)

paper_image1 = Image.open("G:\\F_Y_S_S\\network\\lap\\rock\\paper.png")
paper_image = ImageTk.PhotoImage(paper_image1)

scissors_image1 = Image.open("G:\\F_Y_S_S\\network\\lap\\rock\\scissors.png")
scissors_image = ImageTk.PhotoImage(scissors_image1)
# ---------------------------------------------------------

msg=Label(win,bg="black" , fg="gray", text='Make Your Choice',font=("Courier",25))
msg.place(relx=0.5, rely=0.09, anchor =CENTER)

button1 = Button(win, width=200, height=200, image=stone_image, command= lambda: userChoice(1))
button1.place(relx=0.2, rely=0.35, anchor=CENTER)

button2 = Button(win, width=200, height=200, image=paper_image, command=lambda: userChoice(2))
button2.place(relx=0.5, rely=0.35, anchor=CENTER)

button3 = Button(win, width=200, height=200, command=lambda: userChoice(3),image=scissors_image)
button3.place(relx=0.8, rely=0.35, anchor=CENTER)

ent1 = Entry(win,bg="black" , fg="gray", textvariable=result, width=27, font=('Ubuntu', 24), relief=FLAT)
ent1.place(relx=0.5, rely=0.65, anchor=CENTER) 

ent2 = Entry(win,bg="black" , fg="gray", textvariable=otherPlayerScore, width=2, font=('Ubuntu', 24), relief=FLAT)
ent2.place(relx=0.3, rely=0.85, anchor=CENTER) 

msg2 = Label(win,bg="black" , fg="gray",  text='You ', font=("Courier", 8),relief=FLAT)
msg2.place(relx=0.3, rely=0.79, anchor=CENTER)

msg3 = Label(win,bg="black" , fg="gray", text=' other player ', font=("Courier", 8),relief=FLAT)
msg3.place(relx=0.7, rely=0.79, anchor=CENTER)

msg4 = Label(win,bg="black" , fg="gray", text=' Score Board ', font=("Courier", 18),relief=FLAT)
msg4.place(relx=0.5, rely=0.85, anchor=CENTER)

ent3 = Entry(win,bg="black" , fg="gray", textvariable=yourScore, width=2,font=('Ubuntu', 24),relief=FLAT)
ent3.place(relx=0.7, rely=0.85, anchor=CENTER)

stop = Button(win, text='stop', width=91, command=win.destroy,bg="red", activebackground="red",relief=FLAT)
stop.place(relx=0.5, rely=1, anchor=S)

win.mainloop()