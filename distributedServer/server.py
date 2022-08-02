# Servidor Central
import os
import socket
import json
import signal
import sys
from texttable import Texttable

connection = None

def showTrafficInfo(data):
    tableP = Texttable()
    tableA = Texttable()

    
    tableP.add_rows([['Numero de veiculos', 'Velocidade Media', 'Inf: limite de velocidade', 'Inf: Avanço de sinal'],
    [data['numberCars'][1]['cars'], data['numberCars'][1]['avgSpeed'], data["infractions"][0]['number'], data["infractions"][1]['number']]])
    tableA.add_rows([['Numero de veiculos', 'Inf: limite de velocidade', 'Inf: Avanço de sinal'],
    [data['numberCars'][0]['cars'], data["infractions"][0]['number'], data["infractions"][1]['number']]])
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Mensagem recebida")
    print("Via principal:")
    print(tableP.draw())
    print("Via auxiliar:")
    print(tableA.draw())



def signalHandler(sig, frame):
    print('You pressed Ctrl+C!')
    global connection
    connection.close()
    sys.exit(0)

def socketTcp():
    port = 50000

    # Instancia do server
    serverSocket = socket.socket()
    # Servidor escuta requisições de qualquer ip
    serverSocket.bind(('', port))
    # Socket no modo listen
    serverSocket.listen(3)

    # while True:
    print("Esperando por uma conexão")
    global connection
    conn, address = serverSocket.accept()
    connection = conn
    print(f"Conectado: {address}")

    while True:
        data = conn.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break
        parseData = json.loads(data.decode('utf-8'))
        showTrafficInfo(parseData)
        try:
            conn.send(bytes("ok", 'utf-8'))
        except:
            print("Conexão encerrada")
    conn.close()

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("----- Controle do Cruzamento -------")
    print("1 - Modo de observação do trafego")
    print("2 - Ativar modo de emergencia")
    print("3 - Ativar modo noturno")
    print("0 - Sair")

    return input("Escolha a opção: ")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signalHandler)
    inp = -1
    while inp != 0:
        inp = int(menu())
        print(inp)
        if inp == 1:
            print("Modo obs")
            socketTcp()
            # Observação do trafego
        elif inp == 2:
            # Modo de Emergência
            print("Modo Emergencia")
            pass
        elif inp == 3:
            # Modo noturno
            print("Modo Noturno")
            pass
        elif inp == 0:
            print("Break")
            break
        