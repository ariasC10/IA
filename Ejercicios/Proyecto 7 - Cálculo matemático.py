'''
Calcular el número de botes de pintura que hacen falta para pintar un pared
Pediremos al usuario
    Alto de la pared
    Ancho de la pared
    Cuantos metros cuadrados cubre un bote de pintura
Crearemos una función que calcule el numero de botes
    Fórmula = (Alto * Ancho) / m2 que cubre cada bote
'''
import math

def calcular_botes(alto,ancho,cubre):
    valor = (alto * ancho) / cubre
    numero_botes = math.ceil(valor)
    return numero_botes

alto = int(input("¿Cuál es el alto de la pared? "))
ancho = int(input("¿Cuál es el ancho de la pared? "))
cubre = float(input("¿Cuántos metros cuadrados cubre cada bote de pintura? "))

numero_botes = calcular_botes(alto,ancho,cubre)
print(f"El numero de botes de pintura que tengo que comprar es de {numero_botes}")
