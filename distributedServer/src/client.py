import socket
import json


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
    
    clientSocket = socket.socket()  
    
    message = {"Connect": True}
    clientSocket.connect((host, port))
    clientSocket.send(json.dumps(message).encode()) 
    while True:
        
        data = clientSocket.recv(1024).decode()
        if data != command:
            responseHandle(stateMachine, data)


def infoToSever(info):
    global clientSocket
    if clientSocket != None:
        clientSocket.send(json.dumps(info).encode())
        
def closeClient():      
    clientSocket.close()
