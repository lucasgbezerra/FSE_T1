from speedRadar import SpeedRadar

class Cross:
    def __init__(self, tl1, tl2, btns, sensor, speedRadar):
        self.trafficLight1 = tl1
        self.trafficLight2 = tl2
        self.btns= btns
        self.sensor = sensor
        self.radar1 = speedRadar[0]
        self.radar2 = speedRadar[1]
