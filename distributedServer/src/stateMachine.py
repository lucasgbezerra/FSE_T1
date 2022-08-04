from time import sleep
import RPi.GPIO as GPIO
from time import time
from constants import *

class StateMachine:
    
    def __init__(self, cross):
        self.startTimer = 0
        self.currentState = None
        self.idxState = 0
        self.states = []
        self.nightStates = []
        self.countdown = 0
        self.cross = cross
        self.running = False
        self.mode = 'P'

    def addState(self, sem1, sem2, timer):
        self.states.append((sem1, sem2, timer))

    def set_start(self):
        self.currentState = self.states[self.idxState]
        self.controller(self.currentState[0], self.currentState[1])
        self.countdown = 1
        self.startTimer = time()
        
    def controller(self, l1, l2):
        tl1 = self.cross.trafficLight1
        tl2 = self.cross.trafficLight2
        
        GPIO.output(tl1, False)
        GPIO.output(tl2, False)
        if l1 >= 0 and l2 >= 0:
            GPIO.output(tl1[l1], True)
            GPIO.output(tl2[l2], True)
        
        self.startTimer = time()
        
    def transiction(self):
        if self.idxState == len(self.states) - 3:
            self.idxState = 0
        else:
            self.idxState += 1
        self.currentState = self.states[self.idxState]
        self.countdown = self.currentState[2]
        self.controller(self.currentState[0], self.currentState[1])
    
  
    def nightMode(self):
        if self.idxState == len(self.states) - 2:
            self.idxState = len(self.states) - 1
        else:
            self.idxState = len(self.states) - 2
        self.currentState = self.states[self.idxState]
        self.countdown = self.currentState[2]
        self.controller(self.currentState[0], self.currentState[1])
        
    def emergencyMode(self):
        self.startTimer = -1
        self.idxState = 1
        self.currentState = self.states[self.idxState]
        self.controller(self.currentState[0], self.currentState[1])
        
    def stop(self):
        
        GPIO.output(self.cross.trafficLight1, False)
        GPIO.output(self.cross.trafficLight2, False)
        GPIO.remove_event_detect(self.cross.btns[0])
        GPIO.remove_event_detect(self.cross.btns[1])
        GPIO.remove_event_detect(self.cross.sensor[0])
        GPIO.remove_event_detect(self.cross.sensor[1])
        GPIO.remove_event_detect(self.cross.radar1.sensorA)
        GPIO.remove_event_detect(self.cross.radar1.sensorB)
        GPIO.remove_event_detect(self.cross.radar2.sensorA)
        GPIO.remove_event_detect(self.cross.radar2.sensorB)

        GPIO.cleanup()
        

    def run(self):
        self.running = True
        try:
            # self.set_start()
            while self.running:
                if self.mode.upper() == 'P':
                    if  self.startTimer == 0:
                        self.idxState = 0
                        self.transiction()
                        print(self.mode)
                        
                    if time() - self.startTimer >= self.countdown:
                        self.transiction()
                        
                elif self.mode.upper() == 'N':
                    if  self.startTimer == 0:
                        print(self.mode)
                        self.idxState = len(self.states) - 2
                        self.nightMode()
                        
                        
                    if time() - self.startTimer >= self.countdown:
                        self.nightMode()
                        
                elif self.mode.upper() == 'E':
                    if self.startTimer == 0:
                        print(self.mode)
                        self.emergencyMode()
                        
                    
            print("Stop")
            self.stop()     
        except BaseException as err:
            # print(f"->ERROR: {err}")
            self.stop()
