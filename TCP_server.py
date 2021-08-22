import socket
import datetime
import sys
import platform
import random
from random import choice
from _thread import *
import math
import argparse


from threading import Thread, Lock
from queue import Queue


def IPADDRESS():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    z="Your computer name is:" + str(hostname) + "Your computer IP is: " + str(IPAddr)
    socketKlienti.sendall(str.encode(str(z)))


def PORT():
    z = "The client is using the port " + str(addr[1])
    socketKlienti.sendall(str.encode(z))


def COUNT(a):
    vcount = 0
    ccount = 0
    string = a.lower()
    for i in range (len(string)):
        if string[i] in ('a', "e", "i", "o", "u", "y"):
            vcount = vcount + 1
        elif (string[i] >= 'a' and string[i] <= 'z'):
            ccount = ccount + 1
    z = "vowels " + str(vcount) + " consonants " + str(ccount)
    socketKlienti.sendall(str.encode(z))


def REVERSE(s):
    original = str(s)
    back = str(s[::-1])
    z = "The original text is: " + original + " the back text is " + back
    socketKlienti.sendall(str.encode(z))



def PALINDROME(s):
    string = str(s)
    if string == string[::-1]:
        z = "Sentence is palindrome"
    else:
        z = "Sentence is not palindrome"
    socketKlienti.sendall(str.encode(z))


def TIME():
    y = datetime.datetime.now()
    z = (y.strftime("%d") + '.' + y.strftime("%m") + '.' + y.strftime("%y") + ' ' + y.strftime("%I") + ':' + y.strftime(
        "%M") + ':' + y.strftime("%S") + ' ' + y.strftime("%p"))
    socketKlienti.sendall(str.encode(z))


def GAME():
    z = '('
    sequence = [i for i in range(35)]
    for _ in range(5):
        selection = choice(sequence)
        z = z + str(selection) + ' '
    z = z + ')are 5 random numbers from 35.'
    socketKlienti.sendall(str.encode(z))


def GCF(a,b):
    x = int(a)
    y = int(b)
    gcf = math.gcd(x, y)
    z = "The smallest number is " + str(gcf)
    socketKlienti.sendall(str.encode(z))


def CONVERT(a,b):
    if(a=="CMTOFEET"):
        z=int(b)*0.0328084
    elif(a=="FEETTOCM"):
        z=int(b)/0.0328084
    elif(a=="KMTOMILES"):
        z=int(b)*0.621371
    elif(a=="MILETOKM"):
        z=int(b)/0.621371
    else:
        z = "The request for conversion is not well written."
    socketKlienti.sendall(str.encode(str(z)))

def SQRT(a):
    x = int(a)
    sqrt = math.sqrt(x)
    z = "The root of your number " + str(x) + " is " + str(sqrt)
    socketKlienti.sendall(str.encode(z))

def IOSVERSION():
    z=platform.machine()+"    "+platform.platform()+"    "+platform.node()+"    "+platform.processor()
    socketKlienti.sendall(str.encode(z))

def NOFUN():
    z = ' '
    socketKlienti.sendall(str.encode(str(z)))


def requests(op):
    opi = op
    op = op.split()
    if (op[0] == "IPADDRESS"):
        IPADDRESS()
    elif (op[0] == "PORT"):
        PORT()
    elif (op[0] == "COUNT"):
        COUNT(op[1])
    elif (op[0] == "REVERSE"):
        REVERSE(op[1])
    elif (op[0] == "PALINDROME"):
        PALINDROME(op[1])
    elif (op[0] == "TIME"):
        TIME()
    elif (op[0] == "GAME"):
        GAME()
    elif (op[0] == "GCF"):
          GCF(op[1], op[2])
    elif (op[0] == "CONVERT"):
        CONVERT(op[1], op[2])
    elif (op[0] == "SQRT"):
        SQRT(op[1])
    elif (op[0] == "IOSVERSION"):
        IOSVERSION()
    else:
        NOFUN()


def clientthread(socketKlienti):
    try:
        while True:
            option = socketKlienti.recv(128).decode()
            requests(option)
        socketKlienti.close()
    except:
        print("An error occurred while receiving the request from the client!")


servername = 'localhost'
serverport = 13000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((servername, serverport))
print('================================================================================================')
print('This is the FIEK-TCP Server program.')
print('The server is working on the port ' + str(
    serverport) + '. This port can be changed by the client as needed.')
print('The server is ready to accept requests.')
print('================================================================================================')

while True:
    try:
        serversocket.listen()
        socketKlienti, addr = serversocket.accept()
        print("Client connected to the port " + str(addr[1]))
        start_new_thread(clientthread, (socketKlienti,))
    except:
        print("An error occurred while creating the client socket!")

serversocket.close()

