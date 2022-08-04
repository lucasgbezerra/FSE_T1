# Servidor Central
from texttable import Texttable
from time import sleep
from threading import Thread
import server
import os

def showTrafficInfo():
    
    if len(server.conns) == 0:
        print("Nenhum Servidor Distribuido conectado")
        return
    while True:
        tableP = Texttable()
        tableA = Texttable()

        tableP.add_row(['Cruzamento','Numero de veiculos', 'Velocidade Media', 'Inf: limite de velocidade', 'Inf: Avanço de sinal'])
        tableA.add_row(['Cruzamento','Numero de veiculos', 'Inf: Avanço de sinal'])
    
        for info in server.crossInfo:
            if info != None:
                # print(info)
                tableP.add_row([info['id'], info['principal']['carros'], info['principal']['velocidadeMedia'], info['principal']['limiteVelocidade'], info['principal']['avancoSinal']])
                tableA.add_row([info['id'], info['auxiliar']['carros'], info['auxiliar']['avancoSinal']])
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pressione CTRL-C para SAIR")
        print("Via principal:")
        print(tableP.draw())
        print("Via auxiliar:")
        print(tableA.draw())
        sleep(1)

def menuInfos():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----- Controle do Cruzamento -------")
        print("1 - Modo de observação do trafego")
        print("2 - Ativar modo de emergencia")
        print("3 - Ativar modo noturno")
        print("4 - Ativar modo padrão")
        print("0 - Sair")
        inp = int(input("Escolha a opção: "))
        if inp == 1:
            # Observação do trafego
            showTrafficInfo()
        elif inp == 2:
            # Modo de Emergência
            print("Modo Emergencia")
            server.changeMode('E')
        elif inp == 3:
            # Modo noturno
            print("Modo Noturno")
            server.changeMode('N')
        elif inp == 4:
            # Modo noturno
            print("Modo Padrão")
            server.changeMode('P')
        elif inp == 0:
            break
              

def menu():
    menuThread = Thread(target=menuInfos)
    menuThread.start()
    menuThread.join()