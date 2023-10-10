from socket import *
from threading import *
import random

serverPort = 7
serverName = 'localhost'

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

def handleClient(connectionSocket, address):
    type = connectionSocket.recv(1024).decode()
    type = type.lower()
    firstNumber = int(connectionSocket.recv(1024).decode())
    secondNumber = int(connectionSocket.recv(1024).decode())

    result = 0

    if type == 'random':
        result = random.randint(firstNumber, secondNumber)

    if type == 'add':
        result = firstNumber + secondNumber

    if type == 'subtract':
        result = firstNumber - secondNumber 

    result = str(result)
    print(result)
    connectionSocket.send(result.encode())
    connectionSocket.close()


while True:
    connectionSocket, addr = serverSocket.accept()
    Thread(target=handleClient, args=(connectionSocket, addr)).start()

