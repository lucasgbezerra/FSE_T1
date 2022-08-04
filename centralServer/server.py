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
    print("OK")
    if 'id' not in data.keys():
        return
    if int(data['id']) == 1:
        crossInfo[0] = data
    if int(data['id']) == 2:
        crossInfo[1] = data


# def showTrafficInfo():
#     global crossInfo
#     global conns
#     print(crossInfo)
    
#     if len(conns) == 0:
#         print("Nenhum Servidor Distribuido conectado")
#         return
#     while True:
#         tableP = Texttable()
#         tableA = Texttable()

#         tableP.add_row(['Cruzamento','Numero de veiculos', 'Velocidade Media', 'Inf: limite de velocidade', 'Inf: Avanço de sinal'])
#         tableA.add_row(['Cruzamento','Numero de veiculos', 'Inf: limite de velocidade', 'Inf: Avanço de sinal'])
    
#         for info in crossInfo:
#             if info != None:
#                 tableP.add_row([info['id'], info['numberCars'][1]['cars'], info['numberCars'][1]['avgSpeed'],info["infractions"][0]['number'], info["infractions"][1]['number']])
#                 tableA.add_row([info['id'], info['numberCars'][0]['cars'], info["infractions"][0]['number'], info["infractions"][1]['number']])
#         # os.system('cls' if os.name == 'nt' else 'clear')
#         print("Pressione CTRL-C para SAIR")
#         print("Via principal:")
#         print(tableP.draw())
#         print("Via auxiliar:")
#         print(tableA.draw())
#         sleep(1)


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
