from client import clientProgram
from inputsDetect import *
import signal
import sys
from threading import Thread, current_thread
from setup import *
from functools import partial


def runCross(sm, cross):
    setupStateMachine(sm)
    setupGPIO(cross, sm)
    sm.run()

def signalHandler(sm, sig, frame):
    # print("exit")
    sm.running = False
    sm.stop()
    consts.serverConnection = False
    signal.pthread_kill(current_thread().ident, signal.SIGKILL)
    # sys.exit()


if __name__ == '__main__':
    cross, sm = setup(sys.argv[1])
    host = sys.argv[2]
    port = int(sys.argv[3])
    
    signal.signal(signal.SIGINT, partial(signalHandler, sm))
    threadClient = Thread(target=clientProgram, args=(sm, host, port))
    
    threadClient.start()
    runCross(sm, cross)
    threadClient.join()
    
    
