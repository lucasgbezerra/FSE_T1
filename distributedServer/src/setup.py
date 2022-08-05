import constants as consts
from stateMachine import StateMachine
from speedRadar import SpeedRadar
from cross import Cross
import RPi.GPIO as GPIO
from inputsDetect import *
import json

def setup(file):
    with open(file) as configFile:
        crossing = json.load(configFile)
    
    consts.info['id'] = crossing['crossingId']
    
    speedRadar1 = SpeedRadar(crossing['speedSensor1'][0], crossing['speedSensor1'][1])
    speedRadar2 = SpeedRadar(crossing['speedSensor2'][0], crossing['speedSensor2'][1])
    cross = Cross(crossing['mainTrafficLight'], crossing['secundaryTrafficLight'], crossing['buttons'], crossing['sensor'], [speedRadar1, speedRadar2])
    stateMachine = StateMachine(cross)
    
    return cross, stateMachine

def setupGPIO(cross, sm):
    try:
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(cross.trafficLight1, GPIO.OUT)
        GPIO.setup(cross.trafficLight2, GPIO.OUT)        
        GPIO.setup(cross.btns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # Setup sensores
        GPIO.setup(cross.radar1.sensorA, GPIO.IN)
        GPIO.setup(cross.radar1.sensorB, GPIO.IN)
        GPIO.setup(cross.radar2.sensorA, GPIO.IN)
        GPIO.setup(cross.radar2.sensorB, GPIO.IN)
        GPIO.setup(cross.sensor[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(cross.sensor[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        # Botões Cruzamento
        GPIO.add_event_detect(cross.btns[0], GPIO.RISING, callback=lambda x: detectBtn(cross, sm), bouncetime=200)
        GPIO.add_event_detect(cross.btns[1], GPIO.RISING, callback=lambda x: detectBtn(cross, sm), bouncetime=200)

        # Sensores de velocidade
        GPIO.add_event_detect(cross.radar1.sensorA, GPIO.FALLING, callback=lambda x: detectSpeedSensorA(cross.radar1, sm.currentState), bouncetime=20)
        GPIO.add_event_detect(cross.radar1.sensorB, GPIO.FALLING, callback=lambda x: detectSpeedSensorB(cross.radar1), bouncetime=20)
        GPIO.add_event_detect(cross.radar2.sensorA, GPIO.FALLING, callback=lambda x: detectSpeedSensorA(cross.radar2, sm.currentState), bouncetime=20)
        GPIO.add_event_detect(cross.radar2.sensorB, GPIO.FALLING, callback=lambda x: detectSpeedSensorB(cross.radar2), bouncetime=20)

        # Sensores de passagem
        GPIO.add_event_detect(cross.sensor[0], GPIO.BOTH, callback=lambda x: detectPassSensor(cross, sm), bouncetime=20)
        GPIO.add_event_detect(cross.sensor[1], GPIO.BOTH, callback=lambda x: detectPassSensor(cross, sm), bouncetime=20)
        
        
    except BaseException as err:
        print(f"->ERROR: {err}")

def setupStateMachine(sm):
    sm.addState(consts.RED, consts.RED, consts.BOTH_RED)
    sm.addState(consts.GREEN, consts.RED, consts.MAX_GREEN_RED)
    sm.addState(consts.YELLOW, consts.RED, consts.MIN_MAX_YELLOW)
    sm.addState(consts.RED, consts.RED, consts.BOTH_RED)
    sm.addState(consts.RED, consts.GREEN, consts.MAX_RED_GREEN)
    sm.addState(consts.RED, consts.YELLOW, consts.MIN_MAX_YELLOW)
    sm.addState(consts.RED, consts.YELLOW, consts.MIN_MAX_YELLOW)
    sm.addState(consts.YELLOW, consts.YELLOW, consts.ATTENTION)
    sm.addState(consts.OFF, consts.OFF, consts.ATTENTION)
