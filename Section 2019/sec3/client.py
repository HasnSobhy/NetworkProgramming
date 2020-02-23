
from socket import *
s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7000
s.connect((host,port))
s.send(b'Hello')
s.close()
