'''
Crear la función "pares" que devuelva un array de números pares entre dos valores
como parámetros a la función (inicio y fin)
Utilizar la función "pares" con los números 1 y 30
Utilizar la función "pares con" los números 2 y 40
'''
import numpy as np



def pares(inicio, fin):
    if(inicio % 2 == 0):
        array = np.arange(inicio,fin,2)
    else:
        inicio = inicio + 1
        array = np.arange(inicio,fin,2)
    return array


        


