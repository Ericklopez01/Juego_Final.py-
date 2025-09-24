# 📦 Módulos
import os
import random
from panelControl import cargarPanel
from database.objetos import bonus_random

 
WIDTH_MAPA = 25
HEIGHT_MAPA = 20

# 🧍 Estado inicial del personaje
coordenada_personaje = [10, 25]
direccion = "→"
movimientos = 30

# 🎯 Objetos
simbolo_objeto = "♥"
simbolo_bonus = "+3"
lista_objetos = []
lista_bonus = []

# 🔧 Generar posiciones aleatorias únicas
def generar_objetos(cantidad, excluir, existentes=[]):
    objetos = []
    while len(objetos) < cantidad:
        x = random.randint(0, WIDTH_MAPA - 1)
        y = random.randint(0, HEIGHT_MAPA - 1)
        pos = (x, y)
        if pos not in objetos and pos != tuple(excluir) and pos not in existentes:
            objetos.append(pos)
    return objetos

# 🧹 Limpiar pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# 🗺️ Mostrar el mapa y la información
def mostrar_mapa():
    limpiar_pantalla()

    pos_x = pos_personaje[0]
    pos_y = pos_personaje[1]
    print("┌────────────┬────────────┬────────┬──────────┐")
    print("│ Posición   │ Dirección  │ Movs   │ Objetos  │")
    print(f"│ ({pos_x:02}, {pos_y:02})   │     {direccion}      │   {movimientos:03}   │   {len(lista_objetos) + len(lista_bonus):03}     │")
    print("└────────────┴────────────┴────────┴──────────┘")

    print("┌" + "─" * (WIDTH_MAPA * 2) + "┐")
    for y in range(HEIGHT_MAPA):
        fila = "│"
        for x in range(WIDTH_MAPA):
            pos = (x, y)
            if pos == tuple(pos_personaje):
                fila += direccion + " "
            elif pos in lista_bonus:
                fila += simbolo_bonus
            elif pos in lista_objetos:
                fila += simbolo_objeto + " "
            else:
                fila += "  "
        fila += "│"
        print(fila)
    print("└" + "─" * (WIDTH_MAPA * 2) + "┘")
    print("\nUsa W A S D para moverte. Q para salir (Enter para confirmar).")

# 🕹️ Movimiento del personaje
def mover(tecla):
    global pos_personaje, direccion, movimientos, lista_objetos, lista_bonus
