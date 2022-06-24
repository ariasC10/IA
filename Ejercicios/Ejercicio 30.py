'''
Crear una lista con los valores númericos del 0 al 30
Crear otra lista con los primeros 10 valores de la lista inicial
Crear otra lista con los últimos 10 valores de la lista inicial
Crear un bucle que recorra esta última lista de valores finales
'''

import numpy as np

lista = np.arange(0,30)

principio = lista[0:10]
final = lista[20:30]

for valor in final:
    print(valor)
