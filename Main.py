import os
from database.objetos import objetos_random
from database.objetos import Bonus_random

# Tamaño del mapa
WIDTH_MAPA = 50
HEIGHT_MAPA = 15

# Posición inicial del personaje
coordenada_personaje = [5, 5]
personaje = "►"
movimientos = 30

# Lista de objetos (corazones) dentro del mapa
lista_objetos = [[2, 10], [7, 20], [4, 30], [10, 40]]
ico_objeto = "♥"

# Lista de bonus "+3" dentro del mapa
lista_bonus = [[3, 15], [8, 25]]
ico_bonus = "+3"

def cargar_mapa(Movimiento_personaje):
    global personaje, movimientos

    # Limpiar pantalla
    os.system("cls" if os.name == "nt" else "clear")

    # Movimiento personaje
    if Movimiento_personaje == "w":
        coordenada_personaje[0] = max(0, coordenada_personaje[0] - 1)
        personaje = "▲"
        movimientos += 1
    elif Movimiento_personaje == "s":
        coordenada_personaje[0] = min(HEIGHT_MAPA - 1, coordenada_personaje[0] + 1)
        personaje = "▼"
        movimientos += 1
    elif Movimiento_personaje == "a":
        coordenada_personaje[1] = max(0, coordenada_personaje[1] - 1)
        personaje = "◄"
        movimientos += 1
    elif Movimiento_personaje == "d":
        coordenada_personaje[1] = min(WIDTH_MAPA - 1, coordenada_personaje[1] + 1)
        personaje = "►"
        movimientos += 1

    # Mostrar info
    print(f"[ Posición ] {tuple(coordenada_personaje)}    [ Dirección ] {personaje}    [ Movs ] {movimientos:03}")
    
    # Borde superior
    print(" " + "-" * WIDTH_MAPA)
    
    # Mapa fila por fila
    for fila in range(HEIGHT_MAPA):
        print("|", end="")  
    