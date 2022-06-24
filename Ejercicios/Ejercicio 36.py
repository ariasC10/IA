'''
Crear 
2 arrays con 9 números aleatorios enteros entre los valores 0 y 100
Cambiar el formato de los arrays en una estructra de 3 filas por 3 columnas
Crear un dataframe con esos arrays
Concatenar esos 2 dataframes
'''
import pandas as pd
import numpy as np

array1 = np.random.randint(0,100,9)
array1 = array1.reshape(3,3)

array2 = np.random.randint(0,100,9)
array2 = array1.reshape(3,3)

dataframe1 = pd.DataFrame(array1)
dataframe2 = pd.DataFrame(array2)

dataframe_concat = pd.concat([dataframe1,dataframe2], ignore_index=True)

print(dataframe_concat)
