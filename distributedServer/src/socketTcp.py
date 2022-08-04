from stateMachine import StateMachine
import socket
from threading import Thread

command = 'P' 
def connectClient(conn, stateMachine):
    global command
    try:
        data = conn.recv(1024).decode()
        
        if data != command:
            command = data
            stateMachine.mode = data
            stateMachine.startTimer = 0
            stateMachine.countdown = 0
            
    except socket.error as error:
        print(error)
        conn.close()

def socketTcp(stateMachine):
    port = 12266

    # Instancia do server
    serverSocket = socket.socket()
    # Servidor escuta requisições de qualquer ip
    serverSocket.bind(('', port))
    # Socket no modo listen
    serverSocket.listen(5)
    while True:
        conn, address = serverSocket.accept()
        print(f"Conectado: {address}")
        threadRead = Thread(target= connectClient, args=(conn, stateMachine))
        threadRead.start()
    
