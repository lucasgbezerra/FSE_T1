# Servidor Central
import os
import socket
import json
import signal
import sys
from texttable import Texttable
from time import sleep
from threading import Thread

connection = []
# connectedToSocket = False
crossInfo = [None, None]
mode = 'P'



def trafficInfo(data):
    global crossInfo
    
    if int(data['id']) == 1:
        crossInfo[0] = data
    if int(data['id']) == 2:
        crossInfo[1] = data
    
                
def showTrafficInfo():
    if len(connection) == 0:
        print("Nenhum Servidor Distribuido conectado")
        sleep(1)
        return
    while True:
        tableP = Texttable()
        tableA = Texttable()
    
        tableP.add_row(['Cruzamento','Numero de veiculos', 'Velocidade Media', 'Inf: limite de velocidade', 'Inf: Avanço de sinal'])
        tableA.add_row(['Cruzamento','Numero de veiculos', 'Inf: limite de velocidade', 'Inf: Avanço de sinal'])
    
        for info in crossInfo:
            if info != None:
                tableP.add_row([info['id'], info['numberCars'][1]['cars'], info['numberCars'][1]['avgSpeed'],info["infractions"][0]['number'], info["infractions"][1]['number']])
                tableA.add_row([info['id'], info['numberCars'][0]['cars'], info["infractions"][0]['number'], info["infractions"][1]['number']])
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pressione CTRL-C para SAIR")
        print("Via principal:")
        print(tableP.draw())
        print("Via auxiliar:")
        print(tableA.draw())
        sleep(1)
        

def signalHandler(sig, frame):
    menu()


def closeConnections():
    for conn in connection:
        conn.close()
        
def connectClients(conn):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            parseData = json.loads(data.decode('utf-8'))
            trafficInfo(parseData)

    except socket.error as error:
        print(error)
        closeConnections()

def changeMode(mode):
    global connection
    
    if len(connection) == 0:
        return
    for conn in connection:
        print("Enviado")
        conn.send(bytes(mode, 'utf-8'))
        
def socketTcp():
    port = 10261

    # Instancia do server
    serverSocket = socket.socket()
    # Servidor escuta requisições de qualquer ip
    serverSocket.bind(('', port))
    # Socket no modo listen
    serverSocket.listen(5)
    while True:
        print("Esperando por uma conexão")
        conn, address = serverSocket.accept()
        print(f"Conectado: {address}")
        connection.append(conn)
        threadRead = Thread(target= connectClients, args=(conn, ))
        threadRead.start()
        

    serverSocket.close()
    
# def clientProgram(host, port, message):
    
#     clientSocket = socket.socket()  # instantiate
    
#     clientSocket.connect((host, port))  # connect to the server
#     # while connectedToSocket:
#     clientSocket.send(message.encode())  # send message
#     data = clientSocket.recv(1024).decode()  # receive response
#     if data == 'ok':
#         clientSocket.close()  # close the connection
#         print("close")
#         # print('Mensagem do SERVER: ' + data)  # show in terminal
    
def menuInfos():
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("----- Controle do Cruzamento -------")
    print("1 - Modo de observação do trafego")
    print("2 - Ativar modo de emergencia")
    print("3 - Ativar modo noturno")
    print("4 - Ativar modo padrão")
    print("0 - Sair")
    return input("Escolha a opção: ")
              
def menu():
    inp = int(menuInfos())
    
    while inp != 0:
        print(inp)
        if inp == 1:
            # Observação do trafego
            showTrafficInfo()
        elif inp == 2:
            # Modo de Emergência
            print("Modo Emergencia")
            changeMode('E')
        elif inp == 3:
            # Modo noturno
            print("Modo Noturno")
            changeMode('N')
        elif inp == 4:
            # Modo noturno
            print("Modo Padrão")
            changeMode('P')
        elif inp == 0:
            break
        inp = int(menuInfos())
    

        
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signalHandler)
    threadSocket = Thread(target=socketTcp)
    threadSocket.start()
    menu()
