import socket
import json


command = 'P'
clientSocket = None
connected = True
def responseHandle(stateMachine, data):
    global command
    command = data
    print("Commando", command)
    stateMachine.startTimer = 0
    stateMachine.changeMode = True
    stateMachine.mode = command
    
        
def clientProgram(stateMachine, host, port):
    global clientSocket
    global command
    
    clientSocket = socket.socket()  
    
    message = {"Connect": True}
    clientSocket.connect((host, port))
    print(f"Conectado: {host}:{port}")
    clientSocket.send(json.dumps(message).encode()) 
    try:
        while connected:
            data = clientSocket.recv(1024).decode()
            if data in ['P', 'N', 'E']:
                responseHandle(stateMachine, data)
    except socket.error as error:
        print(error)
        closeClient()

def infoToSever(info):
    global clientSocket
    if clientSocket != None:
        clientSocket.send(json.dumps(info).encode())
        
def closeClient():      
    clientSocket.close()
