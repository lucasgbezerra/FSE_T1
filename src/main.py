import constants as consts
from stateMachine import StateMachine
from speedRadar import SpeedRadar
from cross import Cross
import RPi.GPIO as GPIO
from threading import Thread

def setup(cross):
    try:
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(cross.trafficLight1, GPIO.OUT)
        GPIO.setup(cross.trafficLight2, GPIO.OUT)
    except:
        print('Error')

def setupStateMachine(sm):
    sm.add_state(consts.RED, consts.RED, consts.BOTH_RED)
    sm.add_state(consts.GREEN, consts.RED, consts.MAX_GREEN_RED)
    sm.add_state(consts.YELLOW, consts.RED, consts.MIN_MAX_YELLOW)
    sm.add_state(consts.RED, consts.RED, consts.BOTH_RED)
    sm.add_state(consts.RED, consts.GREEN, consts.MAX_RED_GREEN)
    sm.add_state(consts.RED, consts.YELLOW, consts.MIN_MAX_YELLOW)

def runCross(sm, cross):
    setupStateMachine(sm)
    setup(cross)
    sm.run()


# Cruamento 1
speedRadar1C1 = SpeedRadar(consts.speedSensor1C1[0], consts.speedSensor1C1[1])
speedRadar2C1 = SpeedRadar(consts.speedSensor2C1[0], consts.speedSensor2C1[1])
cross1 = Cross(consts.sem1C1, consts.sem2C1, consts.btnsC1, consts.sensorC1, [speedRadar1C1, speedRadar2C1])

# Cruamento 2
speedRadar1C2 = SpeedRadar(consts.speedSensor1C2[0], consts.speedSensor1C2[1])
speedRadar2C2 = SpeedRadar(consts.speedSensor2C2[0], consts.speedSensor2C2[1])
cross2 = Cross(consts.sem1C2, consts.sem2C2, consts.btnsC2, consts.sensorC2, [speedRadar1C2, speedRadar2C2])


sm1 = StateMachine(cross1)
sm2 = StateMachine(cross2)

# Thread cruzamento 2
threadC2 = Thread(target=runCross,args=(sm2, cross2))

# Semaforo 1
threadC2.start()
runCross(sm1)

