import socket
from socket import *
import threading
import random

serverPort = 12000
serverName = 'oblOpg'

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

def handleClient(connectionSocket, address):
    type = connectionSocket.recv(1024).decode()
    type = type.lower()
    firstNumber = connectionSocket.recv(1024).decode()
    secondNumber = connectionSocket.recv(1024).decode()

    if type == 'random':
        connectionSocket.send(random.randint(firstNumber, secondNumber))

    if type == 'add':
        connectionSocket.send(firstNumber + secondNumber)

    if type == 'subtract':
        connectionSocket.send(firstNumber - secondNumber)  

    connectionSocket.close()


while True:
    connectionSocket, addr = serverSocket.accept()
    handleClient(connectionSocket, addr)

