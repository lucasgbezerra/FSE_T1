# LUZES E SUAS CORRESPONDENCIAS
OFF = -1
RED = 0
YELLOW = 1
GREEN = 2


# TEMPOS ENTRE ESTADOS PRINCIPAL_AUXILIAR
MAX_GREEN_RED = 20
MIN_GREEN_RED = 10
MIN_MAX_YELLOW = 3
MAX_RED_GREEN = 10
MIN_RED_GREEN = 5
BOTH_RED = 1
ATTENTION = 1



# Modelo JSON
info = {
    "id": 0,
    "auxiliar":{
      "carros": 0,
      "avancoSinal": 0
    },
    "principal":{
      "carros": 0,
      "avancoSinal": 0,
      "velocidadeMedia": 0,
      "limiteVelocidade": 0 
    }
}