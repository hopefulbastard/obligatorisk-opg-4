from socket import *

serverPort = 7
serverName = 'oblOpg'

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

type = input('Input "random", "add" or "subtract": ')
firstNumber = input('Input first number:')
secondNumber = input('Input first number:')
clientSocket.send(type.encode())
clientSocket.send(firstNumber.encode())
clientSocket.send(secondNumber.encode())

response = clientSocket.recv(1024)
print('Result: ', response)