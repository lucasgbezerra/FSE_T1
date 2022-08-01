
class SpeedRadar:
    def __init__(self, sensorA, sensorB, speedLimit=60):
        self.sensorA = sensorA
        self.sensorB = sensorB
        self.timeB = 0
        self.timeA = 0
        self.speedLimit = speedLimit
        self.bDistanceA = 1

    def averageSpeed(self):
        speedMS = round(self.bDistanceA/((self.timeA - self.timeB)), 2)
        print("M/s: ",speedMS,"KM/h: ",speedMS*3.6)