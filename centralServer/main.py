from menu import *
from server import socketTcp, signalHandler
from threading import Thread
import signal
import sys

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    
    signal.signal(signal.SIGINT, signalHandler)
    threadSocket = Thread(target=socketTcp, args=(host, port))
    threadSocket.start()
    menu()
    threadSocket.join()
