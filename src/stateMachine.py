from time import sleep
import RPi.GPIO as GPIO
from time import time

class StateMachine:
    
    def __init__(self, cross):
        self.startTimer = 0
        self.currentState = None
        self.idxState = 0
        self.states = []
        self.countdown = 0
        self.cross = cross

    def add_state(self, sem1, sem2, timer):
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
        GPIO.output(tl1[l1], True)
        GPIO.output(tl2[l2], True)
        
        self.startTimer = time()
        
    def transiction(self):
        if self.idxState == len(self.states) -1:
            self.idxState = 0
        else:
            self.idxState += 1
        self.currentState = self.states[self.idxState]
        self.countdown = self.currentState[2]
        self.controller(self.currentState[0], self.currentState[1])
        

    def run(self):
        try:
            self.set_start()
            while True:
                if time() - self.startTimer >= self.countdown:
                    self.transiction()

                    
        except BaseException as err:
            sleep(1)
            # print(f"->ERROR: {err}")
            GPIO.output(self.cross.trafficLight1, False)
            GPIO.output(self.cross.trafficLight2, False)
            # GPIO.remove_event_detect(self.cross.btns[0])
            # GPIO.remove_event_detect(self.cross.btns[1])
            # GPIO.remove_event_detect(self.cross.sensor[0])
            # GPIO.remove_event_detect(self.cross.sensor[1])
            # GPIO.remove_event_detect(self.cross.radar1.sensorA)
            # GPIO.remove_event_detect(self.cross.radar1.sensorB)
            # GPIO.remove_event_detect(self.cross.radar2.sensorA)
            # GPIO.remove_event_detect(self.cross.radar2.sensorB)

            GPIO.cleanup()