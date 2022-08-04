import socket
import json
from time import sleep
from constants import serverConnection, info

command = 'P'
clientSocket = None

def responseHandle(stateMachine, data):
    global command
    command = data
    stateMachine.countdown = 0
    stateMachine.startTimer = 0
    stateMachine.mode = data
        
def clientProgram(stateMachine, host, port):
    global clientSocket
    global command
    
    clientSocket = socket.socket()  # instantiate
    
    message = {"Connect": True}
    clientSocket.connect((host, port))  # connect to the server
    clientSocket.send(json.dumps(message).encode())  # send message
    while True:
        
        data = clientSocket.recv(1024).decode() # receive response
        if data != command:
            responseHandle(stateMachine, data)


def infoToSever(info):
    global clientSocket
    if clientSocket != None:
        clientSocket.send(json.dumps(info).encode())
        
def closeClient():      
    clientSocket.close()  # close the connection
