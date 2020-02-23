#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:29:21 2019

@author: hassan
"""

from socket import *
from threading import Thread



clients_name={}
clients = []
addresses = {}

def accept_incoming_connections():
    while True:
        
        client,client_address=s.accept()
        print("%s:%s has connected ... " %client_address)
        client.send(bytes("Greating From chatRoom..." + "Now Type Your Name and press Enter.." , "utf-8"))
        addresses[client]=client_address
        clients.append(client)
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    name = client.recv(1024).decode('utf-8')
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    sendToAll(msg,client)
    clients_name[client] = name
    
    while True:
        msg = client.recv(1024)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

def sendToAll(msg,con):
    for client in clients:
        if (client != con):
            client.send(msg.encode('utf-8'))

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for client in clients:
        client.send(bytes(prefix, "utf8")+msg)    


host = ""
port = 7000
add = (host, port)

s = socket(AF_INET, SOCK_STREAM)
s.bind(add)

s.listen(5)
print("Waiting for connection...")
ACCEPT_THREAD = Thread(target=accept_incoming_connections)
ACCEPT_THREAD.start()


    
