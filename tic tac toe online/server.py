from socket import*
from _thread import*
import threading
from tkinter import*
from tkinter import messagebox



window = Tk()
window.title("Tic Tac Toe : player X ")
window.geometry("260x320")

s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 8000
s.bind((host, port))
s.listen(5)

global lastWritten

def receive_thread(c):
    while True:        
        x = c.recv(500)
        print("server" + x.decode("utf-8") + " recieved.")
        global lastWritten
        lastWritten = 'O'
        displayRecieved(int(x.decode("utf-8")))
       
def displayRecieved(num):
    bt = [f"button{num}"]
    bt['text'] = 'O'
    check()


c, ad = s.accept()

receive = threading.Thread(target=receive_thread, args=(c,))
receive.start()


        



flag=0
def check():
	global flag
	flag += 1
	b1=button1["text"]
	b2=button2["text"]
	b3=button3["text"]
	b4=button4["text"]
	b5=button5["text"]
	b6=button6["text"]
	b7=button7["text"]
	b8=button8["text"]
	b9=button9["text"]
    
	if(b1==b2 and b2==b3 and b1=='O' or b1==b2 and b2==b3 and b1=='X'):
		win(b1)
	if(b4==b5 and b5==b6 and b4=='O' or b4==b5 and b5==b6 and b4=='X'):
		win(b4)
	if(b7==b8 and b8==b9 and b7=='O' or b7==b8 and b8==b9 and b7=='X'):
		win(b7)
	if(b1==b4 and b4==b7 and b1=='O' or b1==b4 and b4==b7 and b1=='X'):
		win(b1)
	if(b2==b5 and b5==b8 and b2=='O' or b2==b5 and b5==b8 and b2=='X'):
		win(b2)
	if(b3==b6 and b6==b9 and b3=='O' or b3==b6 and b6==b9 and b3=='X'):
		win(b3)
	if(b1==b5 and b5==b9 and b1=='O' or b1==b5 and b5==b9 and b1=='X'):
		win(b1)
	if(b3==b5 and b5==b7 and b3=='O' or b3==b5 and b5==b7 and b3=='X'):
		win(b3)
	if flag == 9:
		messagebox.showinfo("draw")
		window.destroy()


def win(player):
	messagebox.showinfo("Winner is", player )
	window.destroy()


    
turn=1
def clicked1():    
	if button1["text"]==" ":
	   button1["text"]='X'	
	c.send(str(1).encode("utf-8"))
	check()

def clicked2():	
	if button2["text"]==" ":
	   button2["text"]='X'	
	c.send(str(2).encode("utf-8"))
	check()
		
def clicked3():
	if button2["text"]==" ":
	   button2["text"]='X'	
	c.send(str(3).encode("utf-8"))
	check()

def clicked4():
	if button2["text"]==" ":
	   button2["text"]='X'	
	c.send(str(4).encode("utf-8"))
	check()

def clicked5():
	if button2["text"]==" ":
	   button2["text"]='X'
	c.send(str(5).encode("utf-8"))
	check()

def clicked6():
	if button2["text"]==" ":
	   button2["text"]='X'
	c.send(str(6).encode("utf-8"))
	check()

def clicked7():
	if button2["text"]==" ":
	   button2["text"]='X'
	c.send(str(7).encode("utf-8"))
	check()

def clicked8():
	if button2["text"]==" ":
	   button2["text"]='X'
 	c.send(str(8).encode("utf-8"))
	check()
	
def clicked9():
	if button2["text"]==" ":
	   button2["text"]='X'	
	c.send(str(9).encode("utf-8"))
	check()


button1 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked1)
button1.grid(row=0,column=1)

button2 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked2)
button2.grid(row=0,column=2)

button3 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked3)
button3.grid(row=0,column=3)

button4 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked4)
button4.grid(row=1,column=1)

button5 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked5)
button5.grid(row=1,column=2)

button6 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked6)
button6.grid(row=1,column=3)

button7 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked7)
button7.grid(row=2,column=1)

button8 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked8)
button8.grid(row=2,column=2)

button9 = Button(window , text=" " , bg="black" , fg="white" , width=7 , height =4 , font=("Helvtica","15"),command = clicked9)
button9.grid(row=2,column=3)
c.close()

window.mainloop()

