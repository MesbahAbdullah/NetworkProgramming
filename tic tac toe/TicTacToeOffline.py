from tkinter import*
from tkinter import messagebox



window = Tk()
window.title("Tic Tac Toe ")
window.geometry("260x320")

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
	global turn
	if button1["text"]==" ":
		if turn==1:
			turn=2
			button1["text"]='X'
		else:
			turn=1
			button1["text"]='O'
		check()

def clicked2():
	global turn
	if button2["text"]==" ":
		if turn==1:
			turn=2
			button2["text"]='X'
		else:
			turn=1
			button2["text"]='O'
		check()
def clicked3():
	global turn
	if button3["text"]==" ":
		if turn==1:
			turn=2
			button3["text"]='X'
		else:
			turn=1
			button3["text"]='O'
		check()
def clicked4():
	global turn
	if button4["text"]==" ":
		if turn==1:
			turn=2
			button4["text"]='X'
		else:
			turn=1
			button4["text"]='O'
		check()
def clicked5():
	global turn
	if button5["text"]==" ":
		if turn==1:
			turn=2
			button5["text"]='X'
		else:
			turn=1
			button5["text"]='O'
		check()
def clicked6():
	global turn
	if button6["text"]==" ":
		if turn==1:
			turn=2
			button6["text"]='X'
		else:
			turn=1
			button6["text"]='O'
		check()
def clicked7():
	global turn
	if button7["text"]==" ":
		if turn==1:
			turn=2
			button7["text"]='X'
		else:
			turn=1
			button7["text"]='O'
		check()
def clicked8():
	global turn
	if button8["text"]==" ":
		if turn==1:
			turn=2
			button8["text"]='X'
		else:
			turn=1
			button8["text"]='O'
		check()
def clicked9():
	global turn
	if button9["text"]==" ":
		if turn==1:
			turn=2
			button9["text"]='X'
		else:
			turn=1
			button9["text"]='O'
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

window.mainloop()

