import time, datetime
import RPi.GPIO as GPIO
from constants import *
from client import infoToSever

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
    if sensorA == 1:
        speedRadar.timeA = time.time()
        speed = speedRadar.averageSpeed()
        pri = info['principal']
        if pri['carros'] == 0:
            pri['carros'] += 1
            pri['carros']['velocidadeMedia'] += speed
        else:
            info['numberCars'][1]['cars'] += 1
            pri['carros'] += 1
            pri['carros']['velocidadeMedia'] += (pri['velocidadeMedia'] + speed )/2
            
        if currentState[0] == RED:
            print("Furou sinal")
            pri['avancoSinal']
        if speed > speedRadar.speedLimit:
            print("Acima do limite de velocidade")
            pri['limiteVelocidade']
        infoToSever(info)
           

def detectSpeedSensorB(speedRadar):
    sensorB = GPIO.input(speedRadar.sensorB)
   
    if sensorB == 1:
        speedRadar.timeB = time.time()
    

def detectPassSensor(cross, state):
    sensor0 = GPIO.input(cross.sensor[0])
    sensor1 = GPIO.input(cross.sensor[1])
    # print(f"Estado: {state.currentState} | Sensor 0: {sensor0} | Sensor 1: {sensor1}")
    aux = info['auxiliar']
    if state.currentState[1] == RED:
        if sensor1 == 1:
            print("S1: Eperando abrir")
            state.countdown = MIN_GREEN_RED
        if sensor1 == 0:
            aux['avancoSinal'] += 1
            aux['carros'] += 1
            print("S1: Furou sinal")
            infoToSever(info)

    if state.currentState[1] == GREEN:
        if sensor1 == 0:
            aux['avancoSinal'] += 1
            print("S1: Carro passou")
            infoToSever(info)
            

    if state.currentState[1] == RED:
        if sensor0 == 1:
            print("S0: Eperando abrir")
            state.countdown = MIN_GREEN_RED
        if sensor0 == 0:
            print("S0: Furou sinal")
            aux['carros'] += 1
            aux['avancoSinal'] += 1
            infoToSever(info)

    if state.currentState[1] == GREEN:
        if sensor0 == 0:
            print("S0: Carro passou")
            aux['carros'] += 1
            infoToSever(info)

            
                