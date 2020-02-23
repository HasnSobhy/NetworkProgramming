#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:19:33 2019

@author: hassan
"""

from socket import *
s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7000
s.connect((host,port))
while True:
    s.send(input("Clinet: ").encode('utf-8'))
    y=s.recv(2048)
    print("Server: ",y.decode('utf-8'))
s.close()
    
    