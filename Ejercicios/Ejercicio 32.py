'''
Dado el fichero en excel:
1.Copiar los datos al portapapeles
2.Crear un dataframe "datos" con esos datos copiados
3.Mostrar por pantalla, todos los datos del dataframe
4.Mostrar todos los nombres de columnas del dataframe
5.Mostrar la primera fila del dataframe
6.Mostrar la Tercera columna del dataframe
7.Mostrar todas las filas pero solo las columnas "Continente" y "Población"
8.Mostrar las primeras 3 filas del dataframe
9.Mostrar las 2 ultimas filas del dataframe
'''

import pandas as pd

datos = pd.read_clipboard()
print(datos)

print(datos.columns)

print(datos.loc[0])

print(datos['Superficie'])

print(datos.loc[0:3, ['Continente','Población']])

print(datos.loc[0:3])

print(datos.head(3))

print(datos.tail(2))


