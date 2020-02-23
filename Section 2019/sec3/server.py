
from socket import *

s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7000
s.bind((host,port))
s.listen(5)
while True:
    c,ad=s.accept()
    print("connection from ",ad)
    x=c.recv(500)
    print(x)
