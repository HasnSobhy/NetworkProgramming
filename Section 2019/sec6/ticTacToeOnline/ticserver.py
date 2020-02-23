#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 01:27:31 2019

@author: hassan
"""
from _thread import *
import threading
from threading import Thread
from tkinter import*
import tkinter
from tkinter import messagebox
from socket import*

s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000
address = (host, port)
s.bind(address)
s.listen(5)
print("Waiting for new connection...")

wind = tkinter.Tk()
wind.title("player2")
wind.geometry("400x400") 

lb1 = Label(wind, text=" player1 : x ", font="Helvetica")
lb1.grid(row=1, column=0)

lb2 = Label(wind, text=" player2 : o ", font="Helvetica")
lb2.grid(row=2, column=0)


def reset():
    global player
    global turn 
    btn1.config(state = NORMAL)
    btn2.config(state = NORMAL)
    btn3.config(state = NORMAL)
    btn4.config(state = NORMAL)
    btn5.config(state = NORMAL)
    btn6.config(state = NORMAL)
    btn7.config(state = NORMAL) 
    btn8.config(state = NORMAL)
    btn9.config(state = NORMAL)
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" " 
    player=1
    turn=0
	
def win(player):
	messagebox.showinfo("Winner",player+" Is Win")
	reset()
   

turn=0
def check():
    
    global turn
    turn+=1
    if ((btn1["text"]== btn2["text"] and btn2["text"]== btn3["text"] and btn1["text"] =="O") or (btn1["text"]== btn2["text"] and btn2["text"]== btn3["text"] and btn1["text"] =="X")):
        (btn1["text"])
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
    if(turn==9):
        messagebox.showinfo("Game Over","No Winner....")
        reset()        
         
    
   


                 
    
player = 1   
   
    
def clicked1():
    global player
    if (player == 2):
        
        if(btn1['text'] == " "):
            player=1
            btn1['text'] = "O"
            btn1.config(state = DISABLED)
            btn_number = "1"
            c.send(btn_number.encode("utf-8")) 
    check()

def clicked2():
    global player
    if (player == 2):
        
        if(btn2['text'] == " "):
            player=1
            btn2['text'] = "O"
            btn2.config(state = DISABLED)
            btn_number = "2"
            c.send(btn_number.encode("utf-8")) 
    check()

def clicked3():
    global player
    if (player == 2):
        
        if(btn3['text'] == " "):
            player=1
            btn3['text'] = "O"
            btn3.config(state = DISABLED)
            btn_number = "3"
            c.send(btn_number.encode("utf-8")) 
            check()


def clicked4():
    global player
    if (player == 2):
        
        if(btn4['text'] == " "):
            player=1
            btn4['text'] = "O"
            btn4.config(state = DISABLED)
            btn_number = "4"
            c.send(btn_number.encode("utf-8")) 
            check()


def clicked5():
    global player
    if (player == 2):
        
        if(btn5['text'] == " "):
            player=1
            btn5['text'] = "O"
            btn5.config(state = DISABLED)
            btn_number = "5"
            c.send(btn_number.encode("utf-8")) 
            check()

def clicked6():
    global player
    if (player == 2):
        
        if(btn6['text'] == " "):
            player=1
            btn6['text'] = "O"
            btn6.config(state = DISABLED)
            btn_number = "6"
            c.send(btn_number.encode("utf-8")) 
            check()

def clicked7():
    global player
    if (player == 2):
        
        if(btn7['text'] == " "):
            player=1
            btn7['text'] = "O"
            btn7.config(state = DISABLED)
            btn_number = "7"
            c.send(btn_number.encode("utf-8")) 
            check()
def clicked8():
    global player
    if (player == 2):
        
        if(btn8['text'] == " "):
            player=1
            btn8['text'] = "O"
            btn8.config(state = DISABLED)
            btn_number = "8"
            c.send(btn_number.encode("utf-8")) 
            check()

def clicked9():
    global player
    if (player == 2):
        
        if(btn9['text'] == " "):
            player=1
            btn9['text'] = "o"
            btn9.config(state = DISABLED)
            btn_number = "9"
            c.send(btn_number.encode("utf-8")) 
            check()



def rec(c):
    global player
    while True:
        player=2
        btnNumber = c.recv(1024).decode("utf-8")

        if(btnNumber == "1" and btn1['text'] == " "):
            btn1['text'] = "X"
            btn1.config(state = DISABLED)
        if(btnNumber == "2" and btn2['text'] == " "):
            btn2['text'] = "X"
            btn2.config(state = DISABLED)
        if(btnNumber == "3" and btn3['text'] == " "):
            btn3['text'] = "X"
            btn3.config(state = DISABLED)
        if(btnNumber == "4" and btn4['text'] == " "):
            btn4['text'] = "X"
            btn4.config(state = DISABLED)
        if(btnNumber == "5" and btn5['text'] == " "):
            btn5['text'] = "X"
            btn5.config(state = DISABLED)
        if(btnNumber == "6" and btn6['text'] == " "):
            btn6['text'] = "X"
            btn6.config(state = DISABLED)
        if(btnNumber == "7" and btn7['text'] == " "):
            btn7['text'] = "X"
            btn7.config(state = DISABLED)
        if(btnNumber == "8" and btn8['text'] == " "):
            btn8['text'] = "X"
            btn8.config(state = DISABLED)
        if(btnNumber == "9" and btn9['text'] == " "):
            btn9['text'] = "X"
            btn9.config(state = DISABLED)
        check()


btn1=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked1)
btn1.grid(row=0,column=1)

btn2=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked2)
btn2.grid(row=0,column=2)

btn3=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked3)
btn3.grid(row=0,column=3)

btn4=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked4)
btn4.grid(row=1,column=1)

btn5=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked5)
btn5.grid(row=1,column=2)

btn6=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked6)
btn6.grid(row=1,column=3)

btn7=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked7)
btn7.grid(row=2,column=1)

btn8=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked8)
btn8.grid(row=2,column=2)

btn9=Button(wind,text=" ",bg="red",fg="#ffffff",width=4,height=4,font='Times',command=clicked9)
btn9.grid(row=2,column=3)

c, add = s.accept()
print("connection Accepted....")
start_new_thread(rec, (c,))

wind.mainloop()
