#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 01:26:11 2019

@author: hassan
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 00:59:30 2019

@author: hassan
"""

from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread


player=1
turn=1
btnList=list()

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host ="127.0.0.1"
port=7000
s.bind((host,port))
s.listen(5)



wind=Tk()
wind.title("Tic Tac Toe")
wind.geometry("400x300")

l1=Label(wind,text="Player1:X " , font=('Helvetiica',18))
l1.grid(row=0,column=0)
l2=Label(wind,text="Player2:O " , font=('Helvetiica',18))
l2.grid(row=1,column=0)



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


def click(n):
    global btnList
    global player
    global c
    if(player==1):

        btnList[n]['text']='X'
        btnList[n]['state']='disable'
        n=str(n)
        c.send(n.encode('utf-8'))
        player=2
        check()

def receiveThread(sc):
    global btnList
    global turn
    while True:
        n =c.recv(1024)
        n=n.decode('utf-8')
        n=int(n)
        btnList[n]['text']='O'
        btnList[n]['state']='disable'
        player=1
        check() 

def check():
	global turn
	turn+=1
          
	if ((btn1["text"]== btn2["text"] and btn2["text"]== btn3["text"] and btn1["text"] =="O") or (btn1["text"]== btn2["text"] and btn2["text"]== btn3["text"] and btn1["text"] =="X")):
		win(btn1["text"])
	elif ((btn4["text"]== btn5["text"] and btn5["text"]== btn6["text"] and btn4["text"] =="O") or (btn4["text"]== btn5["text"] and btn5["text"]== btn6["text"] and btn4["text"] =="X")):
		win(btn4["text"])

	elif ((btn7["text"]== btn8["text"] and btn8["text"]== btn9["text"] and btn7["text"] =="O") or (btn7["text"]== btn8["text"] and btn8["text"]== btn9["text"] and btn7["text"] =="X")):
		win(btn7["text"])

	elif ((btn1["text"]== btn4["text"] and btn4["text"]== btn7["text"] and btn1["text"] =="O") or (btn1["text"]== btn4["text"] and btn4["text"]== btn7["text"] and btn1["text"] =="X")):
		win(btn1["text"])

	elif ((btn2["text"]== btn5["text"] and btn5["text"]== btn8["text"] and btn2["text"] =="O") or (btn2["text"]== btn5["text"] and btn5["text"]== btn8["text"] and btn2["text"] =="X")):
		win(btn2["text"])

	elif ((btn3["text"]== btn6["text"] and btn6["text"]== btn9["text"] and btn3["text"] =="O") or (btn3["text"]== btn6["text"] and btn6["text"]== btn9["text"] and btn3["text"] =="X")):
		win(btn3["text"])

	elif ((btn1["text"]== btn5["text"] and btn5["text"]== btn9["text"] and btn1["text"] =="O") or (btn1["text"]== btn5["text"] and btn5["text"]== btn9["text"] and btn1["text"] =="X")):
		win(btn1["text"])

	elif ((btn3["text"] == btn5["text"] and btn5["text"]== btn7["text"] and btn3["text"] =="O") or (btn3["text"]== btn5["text"] and btn5["text"]== btn7["text"] and btn3["text"] =="X")):
		win(btn3["text"])
        
    
        
       
	
def win(player):
	messagebox.showinfo("Winner",player+" Is Win")
	reset()    






btn1=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(0))
btn1.grid(row=0,column=1)

btn2=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(1))
btn2.grid(row=0,column=2)

btn3=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(2))
btn3.grid(row=0,column=3)

btn4=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(3))
btn4.grid(row=1,column=1)

btn5=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(4))
btn5.grid(row=1,column=2)

btn6=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(5))
btn6.grid(row=1,column=3)

btn7=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(6))
btn7.grid(row=2,column=1)

btn8=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(7))
btn8.grid(row=2,column=2)

btn9=Button(wind,text="",bg="#3c3c3c",fg="#ffffff",width=4,height=4,font='Helvetiica',command=lambda:click(8))
btn9.grid(row=2,column=3)




btnList.append(btn1)
btnList.append(btn2)
btnList.append(btn3)
btnList.append(btn4)
btnList.append(btn5)
btnList.append(btn6)
btnList.append(btn7)
btnList.append(btn8)
btnList.append(btn9)

    


while True:
    c,ad = s.accept()
    th=Thread(target=receiveThread,args=(c,))
    th.start()
    wind.mainloop()
    

 
