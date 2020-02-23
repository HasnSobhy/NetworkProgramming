#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:04:13 2019

@author: hassan
"""
from socket import *
from _thread import *
import threading

def recieve_thread(c):
    while True:
        x=c.recv(500) 
        print("Client: ",x.decode('utf-8'),)
		

def client_thread(c):
	recieve=threading.Thread(target=recieve_thread,args=(c,))
	recieve.start()
	while True:
          c.send(input("Server: ").encode('utf-8'))
      
	
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host="127.0.0.1"
port=7000
s.bind((host,port))
s.listen(5)
print("Waiting for connection")
try:   
    while True:
        c,ad=s.accept()
        print("Connection sucessfuly from ",ad[0])
      
        start_new_thread(client_thread,(c,))
       
except KeyboardInterrupt :
    print("chat is finished")
    s.close()
    
    
    
    
