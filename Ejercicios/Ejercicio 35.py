'''
Vamos a filtrar datos en un DataFrame

Crearemos una lista de 50 valores aleatorios enteros entre los valores 0 y 100
Convertimos esta lista en un dataframe con 5 filas y 10 columnas
Filtraremos los datos del dataframe para visualizar solo los valores que sean mayores de 50
'''

import pandas as pd
import numpy as np

lista_valores = np.random.randint(0,100,50)

lista_valores.resize(5,10)

dataframe = pd.DataFrame(lista_valores)

print(dataframe[dataframe > 50])
