import socket
import sys
import json
import signal
from time import sleep
from constants import connection, info

serverConnection = True

# def getJson():
#     with open('file.json') as jsonFile:
#         data = json.load(jsonFile)
#     jsonFile.close()
#     return data

# def signalHandler(sig, frame):
#     print('You pressed Ctrl+C!')
#     global connection
#     connection.close()
#     sys.exit(0)


def clientProgram():
    host = '192.168.0.118'  # as both code is running on same pc
    port = 50000  # socket server port number
    
    clientSocket = socket.socket()  # instantiate
    
    clientSocket.connect((host, port))  # connect to the server
    global connection
    connection = clientSocket


    while serverConnection:
        message = json.dumps(info)
        
        clientSocket.send(message.encode())  # send message
        data = clientSocket.recv(1024).decode()  # receive response

        print('Mensagem do SERVER: ' + data)  # show in terminal
        sleep(2)

    clientSocket.close()  # close the connection
