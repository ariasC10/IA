'''
Juego piedra, papel o tijera

El usuario elige también su opción
Ordenador elige una opción aleatoria

Resultado
La tijera gana al papel
El papel gana a la piedra
La piedra gana a la tijera
'''

import random

print("Bienvenidos al juego")
usuario = int(input("Escoge la opción. Escribe '0' para piedra, '1' para papel y '2' para tijera: "))

ordenador = random.randint(0,2)

print("Usuario =" + str(usuario))

print(f"Ordenador = {ordenador}")

if usuario == 0 and ordenador == 2:
    print("Ha ganado el usuario")
elif usuario > ordenador:
    print("Ha ganado el usuario")
elif usuario == ordenador:
    print("Empate")
else:
    print("Ha ganado el ordenador")
