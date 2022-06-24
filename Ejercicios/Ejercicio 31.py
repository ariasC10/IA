'''
Tenemos 3 clases "clase1", "clase2", "clase3"
Vamos a generar un número aleatorio de alumnos por clase
Para obtener un numero aleatorio utilizaremos
    np.random.randint(minimo,maximo,numero)

Crear una serie de clases y alumnos
Y utilizar el indice de la serie creada para saber el numero de alumnos de la clase 2
'''
import pandas as pd
import numpy as np

minimo = 10
maximo = 40
numero = 3

alumnos = np.random.randint(minimo,maximo,numero)

clases = ['clase1','clase2','clase3']

serie = pd.Series(alumnos, index=clases)
