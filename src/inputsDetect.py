import time, datetime
import RPi.GPIO as GPIO
from constants import *

def detectBtn(cross, state):
    timedate = datetime.datetime.now().strftime('%H:%M:%S %Y/%m/%d %a')
    if GPIO.input(cross.btns[0]) == 1:
        print("Btn 1:", timedate)
        if state.currentState[1] == GREEN:
            state.countdown = MIN_GREEN_RED
    if GPIO.input(cross.btns[1]) == 1:
        print("Btn 2:", timedate)
        if state.currentState[0] == GREEN:
            state.countdown = MIN_RED_GREEN


def detectSpeedSensorA(speedRadar, currentState):
    sensorA = GPIO.input(speedRadar.sensorA)
    if sensorA == 0:
        speedRadar.timeA = time.time()
        speed = speedRadar.averageSpeed()

        if currentState[0] == RED:
            print("Furou sinal")
        if speed > speedRadar.speedLimit:
            print("Acima do limite de velocidade")


def detectSpeedSensorB(speedRadar):
    sensorB = GPIO.input(speedRadar.sensorB)
   
    if sensorB == 0:
        speedRadar.timeB = time.time()

def detectPassSensor(cross, state):
    sensor0 = GPIO.input(cross.sensor[0])
    sensor1 = GPIO.input(cross.sensor[1])
    print(f"Estado: {state.currentState} | Sensor 0: {sensor0} | Sensor 1: {sensor1}")
    
    if state.currentState[1] == RED:
        if sensor1 == 1:
            print("S1: Eperando abrir")
            state.countdown = MIN_GREEN_RED
        if sensor1 == 0:
            print("S1: Furou sinal")

    if state.currentState[1] == GREEN:
        if sensor1 == 0:
            print("S1: Carro passou")

    if state.currentState[1] == RED:
        if sensor0 == 1:
            print("S0: Eperando abrir")
            state.countdown = MIN_GREEN_RED
        if sensor0 == 0:
            print("S0: Furou sinal")

    if state.currentState[1] == GREEN:
        if sensor0 == 0:
            print("S0: Carro passou")
    