# Importando el mdulo os
import os
from data.Datos import lista_menu
# Limpiar la terminal
os.system("clear")

estado = True

# Bucle que depende de la variable estado
while estado:

print("+---------------------------------------+")
print("|ERICK             2025              |")
print("|                                    |")
print(f"|[1]: {Lista_menu[0]}")
print(f"|[2]: {Lista_menu[1]}")
print(f"|[3]: {Lista_menu[2]}")
print(f"|[0]: salir")

r = int(imput("|[?]: "))
if r == 0:
    estado = False

print("|[Saliendo del programa...]")
