#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:09:02 2019

@author: hassan
"""

#from tkinter import font
from socket import *
import tkinter
from threading import Thread


#myfont=font.Font(size=5)

def receive():
    while True:
        msg=client_socket.recv(1024).decode('utf-8')
        msg_list.insert(tkinter.END, msg)


def send(event=None):
    msg=my_msg.get()
    my_msg.set("")
    client_socket.send(msg.encode('utf-8'))
    if msg == "{quit}":
        client_socket.close()
        wind.quit()

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


wind = tkinter.Tk()
wind.title("Chat App")   

msg_frame=tkinter.Frame(wind)
my_msg=tkinter.StringVar()
my_msg.set("")
scrollbar=tkinter.Scrollbar(msg_frame)


msg_list =tkinter.Listbox(msg_frame, height=40, width=80,yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
msg_frame.pack()
 

entry_field=tkinter.Entry(wind,textvariable=my_msg)
entry_field.bind("<Return>",send)
entry_field.pack()

send_button = tkinter.Button(wind, text="Send", command=send)
send_button.pack()

wind.protocol("WM_DELETE_WINDOW", on_closing)


host=input("Enter host: ")
port=input("Enter port: ")
if not port:
    port = 7000
else:
    port = int(port)

client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect((host,port))

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()    
    
