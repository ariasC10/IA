'''
Subasta para calcular la apuesta más alta

Flujo de trabajo:
-Mensaje de bienvenida al programa
-Preguntar por el nombre del primer aportante
-Preguntar por el precio de su apuesta
-Añadir el nombre (clave) y su apuesta (valor) a un diccionario de apuestas
-Borrar la pantalla
-Preguntar si hay más personas que quieren hacer su apuesta (si,no) (bucle hasta respuesta == no)
    Si respuesta == si
        -preguntar nombre de la otra persona
        -preguntar por su apuesta
        -añadir el nombre (clave) y su apuesta (valor) al diccionario de apuestas creado al principio
        -borrar la pantalla
    Si respuesta == no
        -mostrar la apuesta ganadora de la subasta
        --fin del programa

'''
import os

def calcular_ganador(apuestas):
    apuesta_maxima=0
    ganador=""
    for clave in apuestas:
        precio_apuesta = apuestas[clave]
        if precio_apuesta > apuesta_maxima:
            apuesta_maxima = precio_apuesta
            ganador = clave
    print(f"El ganador es {ganador} con un precio de {apuesta_maxima}")

print("Bienvenidos a la subasta")
apuestas = {}
mas_apuestas = True

while mas_apuestas:
    nombre = input("Nombre del apostante: ")
    precio = float(input("Precio de la apuesta: "))
    apuestas[nombre] = precio

    pregunta = input("¿Alguien más desea hacer una apuesta?. Escribe 'si' o 'no': ")
    if pregunta == 'si':
        os.system('clear')
    elif pregunta == 'no':
        mas_apuestas = False

os.system('clear')
calcular_ganador(apuestas)
    
