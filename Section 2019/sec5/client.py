#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:19:33 2019

@author: hassan
"""

from socket import *
from _thread import *
import threading

def recieve_thread(s):
    while True:
        y=s.recv(500)
        print("Server: ",y.decode('utf-8'))
	
 
s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7000
s.connect((host,port))

recieve=threading.Thread(target=recieve_thread,args=(s,))
recieve.start()
while True:
    s.send(input("Clinet: ").encode('utf-8'))
   

    
    
