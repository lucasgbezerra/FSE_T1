
class SpeedRadar:
    def __init__(self, sensorA, sensorB, speedLimit=60):
        self.sensorA = sensorA
        self.sensorB = sensorB
        self.timeB = 0
        self.timeA = 0
        self.speedLimit = speedLimit
        self.bDistanceA = 1

    def averageSpeed(self):
        deltaT = self.timeA - self.timeB 
        speedMS = self.bDistanceA / deltaT
        speedKmH = speedMS * 3.6
        print("m/s: ",round(speedMS, 2),"Km/h: ",round(speedKmH, 2))
        self.reset()

        return speedKmH
        
    def reset(self):
        self.timeA = 0
        self.timeB = 0