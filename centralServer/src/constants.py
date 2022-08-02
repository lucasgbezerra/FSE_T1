# LUZES E SUAS CORRESPONDENCIAS
RED = 0
YELLOW = 1
GREEN = 2

# TEMPOS ENTRE ESTADOS PRINCIPAL_AUXILIAR
MAX_GREEN_RED = 20
MIN_GREEN_RED = 1
MIN_MAX_YELLOW = 3
MAX_RED_GREEN = 10
MIN_RED_GREEN = 1
BOTH_RED = 1

# BOTOES [1, 2]
btnsC1 = [8, 7]
btnsC2 = [10, 9]

# SEMAFORO [VERMELHO, AMARELO, VERDE]
sem1C1 = [12, 16, 20]
sem2C1 = [21, 26, 1]
sem1C2 = [6, 5, 0]
sem2C2 = [11, 3, 2]

# SENSOR DE VELOCIDADE [A, B]
speedSensor1C1 = [18, 23]
speedSensor2C1 = [24, 25]
speedSensor1C2 = [27, 22]
speedSensor2C2 = [13, 19]

# SENSOR DE PASSAGEM
sensorC1 = [14, 15]
sensorC2 = [4, 17]

teste = True

connection = None

# Modelo JSON
info = {
    "id": 1,
    "numberCars": [
        {
        "road": "Auxiliar",
        "cars": 0
        },
        {
        "road": "Principal",
        "cars": 0,
        "avgSpeed": 0
        }
    ],
     "infractions": [
    {
      "name": "Limite de velocidade",
      "number": 0
    },
    {
      "name": "Avanço de sinal vermelho",
      "number": 0
    }
  ]
}