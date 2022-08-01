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
    
        

def detectSpeedSensor(speedRadar, currentState):
    if GPIO.input(speedRadar.sensorB) == 1:
        speedRadar.timeB = time.time()
    if GPIO.input(speedRadar.sensorA) == 1:
        speedRadar.timeA = time.time()
        speedRadar.averageSpeed()
        if currentState[0] == RED:
            print("Furou sinal")
        # TO-DO verificar limite de velocidade e enviar ao server central

def detectPassSensor(cross, state):
    # Tratar o tempo de diferença entre furar sinal e estar parado
    if GPIO.input(cross.sensor[0]) == 1 or GPIO.input(cross.sensor[1]) == 1:
        if state.currentState[1] == RED:
            print("Aux: Furou sinal")
        else: 
            print("Aux: Carro passou")

    if GPIO.input(cross.sensor[0]) == 0 or GPIO.input(cross.sensor[1]) == 0:
        if state.currentState[0] == GREEN:
            state.countdown = MIN_GREEN_RED
