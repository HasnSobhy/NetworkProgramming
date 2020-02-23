from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread

player=1
turn=1



def reset():
	global player
	global turn 
	btn1["text"]=""
	btn2["text"]=""
	btn3["text"]=""
	btn4["text"]=""
	btn5["text"]=""
	btn6["text"]=""
	btn7["text"]=""
	btn8["text"]=""
	btn9["text"]=""
	player=1
	turn=1
   



def check():
	global turn
	turn+=1
          
	if ((btn1["text"]== btn2["text"] and btn2["text"]== btn3["text"] and btn1["text"] =="O") or (btn1["text"]== btn2["text"] and btn2["text"]== btn3["text"] and btn1["text"] =="X")):
		win(btn1["text"])
	if ((btn4["text"]== btn5["text"] and btn5["text"]== btn6["text"] and btn4["text"] =="O") or (btn4["text"]== btn5["text"] and btn5["text"]== btn6["text"] and btn4["text"] =="X")):
		win(btn4["text"])

	if ((btn7["text"]== btn8["text"] and btn8["text"]== btn9["text"] and btn7["text"] =="O") or (btn7["text"]== btn8["text"] and btn8["text"]== btn9["text"] and btn7["text"] =="X")):
		win(btn7["text"])

	if ((btn1["text"]== btn4["text"] and btn4["text"]== btn7["text"] and btn1["text"] =="O") or (btn1["text"]== btn4["text"] and btn4["text"]== btn7["text"] and btn1["text"] =="X")):
		win(btn1["text"])

	if ((btn2["text"]== btn5["text"] and btn5["text"]== btn8["text"] and btn2["text"] =="O") or (btn2["text"]== btn5["text"] and btn5["text"]== btn8["text"] and btn2["text"] =="X")):
		win(btn2["text"])

	if ((btn3["text"]== btn6["text"] and btn6["text"]== btn9["text"] and btn3["text"] =="O") or (btn3["text"]== btn6["text"] and btn6["text"]== btn9["text"] and btn3["text"] =="X")):
		win(btn3["text"])

	if ((btn1["text"]== btn5["text"] and btn5["text"]== btn9["text"] and btn1["text"] =="O") or (btn1["text"]== btn5["text"] and btn5["text"]== btn9["text"] and btn1["text"] =="X")):
		win(btn1["text"])

	if ((btn3["text"] == btn5["text"] and btn5["text"]== btn7["text"] and btn3["text"] =="O") or (btn3["text"]== btn5["text"] and btn5["text"]== btn7["text"] and btn3["text"] =="X")):
		win(btn3["text"])
   
    
    
        
	
def win(player):
	messagebox.showinfo("Winner",player+" Is Win")
	reset()
   

def cliked1():
	global player
	if (btn1["text"]==""):
		if(player==1):
			player=2
			btn1["text"]='X'
		else:
			player=1
			btn1["text"]='O'
		check()	
		
def cliked2():
	global player
	if (btn2["text"]==""):
		if(player==1):
			player=2
			btn2["text"]='X'
		else:
			player=1
			btn2["text"]='O'
		check()	
			
def cliked3():
	global player
	if (btn3["text"]==""):
		if(player==1):
			player=2
			btn3["text"]='X'
		else:
			player=1
			btn3["text"]='O'
		check()	
			
def cliked4():
	global player
	if (btn4["text"]==""):
		if(player==1):
			player=2
			btn4["text"]='X'
		else:
			player=1
			btn4["text"]='O'
		check()	
			
def cliked5():
	global player
	if (btn5["text"]==""):
		if(player==1):
			player=2
			btn5["text"]='X'
		else:
			player=1
			btn5["text"]='O'
		check()	
			
def cliked6():
	global player
	if (btn6["text"]==""):
		if(player==1):
			player=2
			btn6["text"]='X'
		else:
			player=1
			btn6["text"]='O'
		check()	
			
def cliked7():
	global player
	if (btn7["text"]==""):
		if(player==1):
			player=2
			btn7["text"]='X'
		else:
			player=1
			btn7["text"]='O'
		check()	
			
def cliked8():
	global player
	if (btn8["text"]==""):
		if(player==1):
			player=2
			btn8["text"]='X'
		else:
			player=1
			btn8["text"]='O'
		check()	
			
def cliked9():
	global player
	if (btn9["text"]==""):
		if(player==1):
			player=2
			btn9["text"]='X'
		else:
			player=1
			btn9["text"]='O'
		check()	
			
		
			


wind=Tk()
wind.title("Tic Tac Toe")
wind.geometry("400x300")

l1=Label(wind,text="Player1:X " , font=('Helvetiica',18))
l1.grid(row=0,column=0)
l2=Label(wind,text="Player2:O " , font=('Helvetiica',18))
l2.grid(row=1,column=0)

btn1=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked1)
btn1.grid(row=0,column=1)

btn2=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked2)
btn2.grid(row=0,column=2)

btn3=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked3)
btn3.grid(row=0,column=3)

btn4=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked4)
btn4.grid(row=1,column=1)

btn5=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked5)
btn5.grid(row=1,column=2)

btn6=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked6)
btn6.grid(row=1,column=3)

btn7=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked7)
btn7.grid(row=2,column=1)

btn8=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked8)
btn8.grid(row=2,column=2)

btn9=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=cliked9)
btn9.grid(row=2,column=3)

wind.mainloop()
