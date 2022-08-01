import constants as consts
from stateMachine import StateMachine
from speedRadar import SpeedRadar
from cross import Cross


# Cruamento 1
speedRadar1C1 = SpeedRadar(consts.speedSensor1C1[0], consts.speedSensor1C1[1])
speedRadar2C1 = SpeedRadar(consts.speedSensor2C1[0], consts.speedSensor2C1[1])
cross1 = Cross(consts.sem1C1, consts.sem2C1, consts.btnsC1, consts.sensorC1, [speedRadar1C1, speedRadar2C1])


sm1 = StateMachine(cross1)


def setupStateMachine():
    # Cruzamento 1
    sm1.add_state(consts.RED, consts.RED, consts.BOTH_RED)
    sm1.add_state(consts.GREEN, consts.RED, consts.MAX_GREEN_RED)
    sm1.add_state(consts.YELLOW, consts.RED, consts.MIN_MAX_YELLOW)
    sm1.add_state(consts.RED, consts.RED, consts.BOTH_RED)
    sm1.add_state(consts.RED, consts.GREEN, consts.MAX_RED_GREEN)
    sm1.add_state(consts.RED, consts.YELLOW, consts.MIN_MAX_YELLOW)


#Cria Thread
setupStateMachine()
sm1.run()

