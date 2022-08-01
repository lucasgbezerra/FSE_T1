from speedRadar import SpeedRadar

class Cross:
    def __init__(self, tl1, tl2, btns, sensor, speedRadar):
        self.trafficLight1 = tl1
        self.trafficLight2 = tl2
        self.btns= btns
        self.sensor = sensor
        # self.speedSensor1 = speedSensor1
        # self.speedSensor2 = speedSensor2
        # self.timeSensor1 = [0, 0]
        # self.timeSensor2 = [0, 0]
        # self.speedLimit = speedLimit
        # self.bDistanceA = 1
        self.radar1 = speedRadar[0]
        self.radar2 = speedRadar[1]
    # def averageSpeed(self, speedSensor):
    #     if speedSensor == self.speedSensor1:
    #         speedMS = round(self.bDistanceA/((self.timeSensor1 - self.timeB)), 2)
    #         print("M/s: ",speedMS,"KM/h: ",speedMS*3.6)