import socket
import json
from time import sleep
from constants import connection, info

serverConnection = True

def clientProgram():
    host = '192.168.0.118'  # as both code is running on same pc
    port = 10261  # socket server port number
    
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
