import random

# random entre 1 25
# random entre 1 20
def numero_alto():
    return random.randint(0,19)

def numero_ancho():
    return random.randint(0,24)

# Objetos
objetos_random = [
    [numero_alto(), numero_ancho],
    [numero_alto(), numero_ancho],
    [numero_alto(), numero_ancho],
    [numero_alto(), numero_ancho]
]

# Bonus 
bonus_random = [
    [numero_alto(), numero_ancho],
    [numero_alto(), numero_ancho],
    [numero_alto(), numero_ancho],
    [numero_alto(), numero_ancho]
]


