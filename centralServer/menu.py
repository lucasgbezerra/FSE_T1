# Servidor Central
import signal
from texttable import Texttable
from time import sleep
from threading import Thread, current_thread
import server
import os
import sys

runningObsMode = True
def showTrafficInfo():
    global runningObsMode
    
    if len(server.conns) == 0:
        print("Nenhum Servidor Distribuido conectado")
        sleep(1)
        return
    while runningObsMode:
        tableP = Texttable()
        tableA = Texttable()

        tableP.add_row(['Cruzamento','Numero de veiculos', 'Velocidade Media', 'Inf: limite de velocidade', 'Inf: Avanço de sinal'])
        tableA.add_row(['Cruzamento','Numero de veiculos', 'Inf: Avanço de sinal'])
    
        for info in server.crossInfo:
            if info != None:
                tableP.add_row([info['id'], info['principal']['carros'], info['principal']['velocidadeMedia'], info['principal']['limiteVelocidade'], info['principal']['avancoSinal']])
                tableA.add_row([info['id'], info['auxiliar']['carros'], info['auxiliar']['avancoSinal']])
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pressione CTRL-Z para SAIR")
        print("Via principal:")
        print(tableP.draw())
        print("Via auxiliar:")
        print(tableA.draw())
        sleep(1)
        
def exitMenu():
    os.kill(os.getpid(), signal.SIGINT)

def menuInfos():
    global runningObsMode
    inp = -1
    
    while inp != 0:
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
            runningObsMode = True
            showTrafficInfo()
        elif inp == 2:
            # Modo de Emergência
            print("Modo Emergencia Ativado")
            server.changeMode('E')
        elif inp == 3:
            # Modo noturno
            print("Modo Noturno Ativado")
            server.changeMode('N')
        elif inp == 4:
            # Modo noturno
            print("Modo Padrão Ativado")
            server.changeMode('P')
        else:
            break
    exitMenu()
def backToMenu(sig, frame):
    global runningObsMode
    runningObsMode = False

def menu():
    signal.signal(signal.SIGTSTP, backToMenu)
    menuThread = Thread(target=menuInfos)
    menuThread.start()
    menuThread.join()
    