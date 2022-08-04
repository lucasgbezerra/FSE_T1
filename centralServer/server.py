from http import client
from threading import Thread
import socket
import json
import sys

conns = []
crossInfo = [None, None]
clients = True
serverConn = True
def signalHandler(sig, frame):
    global serverConn
    global clients
    serverConn = False
    clients = False
    if len(conns) > 0:
        closeConnections()
    sys.exit(0)
        
def socketTcp(host, port):
    global serverConn
    
    # Instancia do serverConn
    serverSocket = socket.socket()
    # Servidor escuta requisições de qualquer ip
    serverSocket.bind(('', port))
    # Socket no modo listen
    serverSocket.listen(1)
    while serverConn:
        conn, address = serverSocket.accept()
        print(f"Conectado: {address}")
        conns.append(conn)
        threadRead = Thread(target= connectClients, args=(conn, ))
        threadRead.start()  
    
def trafficInfo(data):
    global crossInfo
    if 'id' not in data.keys():
        return
    if int(data['id']) == 1:
        crossInfo[0] = data
    if int(data['id']) == 2:
        crossInfo[1] = data


def closeConnections():
    global conns
    global clients
    for conn in conns:
        conn.close()
           
def connectClients(conn):
    try:
        while clients:
            data = conn.recv(1024)
            if not data:
                break
            parseData = json.loads(data.decode('utf-8'))
            trafficInfo(parseData)

    except socket.error as error:
        print(error)
        closeConnections()
        
def changeMode(mode):
    global conns
    
    for conn in conns:
        conn.send(bytes(mode, 'utf-8'))
