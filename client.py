import socket
import os


def power(a, b, P):
    if (b == 1):
        return a

    else:
        return ((pow(a, b)) % P)


print("************CLIENT PROGRAM STARTED ******************")
s = socket.socket()
host = socket.gethostname()  # server hostname
# host='127.0.0.1'
port = 12000  # same as server
s.connect((host, port))
print("Connected to : ", host, port)
# fileToSend = open("ToSend.txt","r")
# content = fileToSend.read()
P = 941
q = 627
b = int(input('Enter Your private Key: '))
y = power(q, b, P)
s.send(str(y).encode())
x = int(s.recv(100).decode())
kb = power(x, b, P)
print('Secret Key of Bob: '	, kb)
print("************CLIENT PROGRAM ENDED ******************")
