'''
1.Crear una lista de números del 10 al 19
2.Crear otra lista con números del 50 al 59
3.Crear una matriz de 2x10 con las listas anteriores
4.Crear otra matriz que cuyos valores sean iguales a la matriz anterior multiplicados por 2
'''

import numpy as np

lista1 = [10,11,12,13,14,15,16,17,18,19]
lista2 = [50,51,52,53,54,55,56,57,58,59]

lista_doble = (lista1,lista2)

array_doble = np.array(lista_doble)

array_doble_C = array_doble.copy()

array_mult = array_doble_C * 2

print(array_doble)
print(array_mult)
