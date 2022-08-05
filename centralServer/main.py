from menu import *
from server import socketTcp, signalHandler
from threading import Thread, current_thread
import signal
import sys

if __name__ == '__main__':
    port = int(sys.argv[1])
    
    
    signal.signal(signal.SIGINT, signalHandler)
    threadSocket = Thread(target=socketTcp, args=(port))
    threadSocket.start()
    menu()
    threadSocket.join()
