'''
Leer fichero adjunto "poblacion.xlsx" y cargar los datos en un dataframe
Con esos datos, visualizar cual es la ciudad más poblada en América

Leer el fichero adjunto "poblacion.csv" y cargar los datos en un dataframe
Con esos datos, visualizar cual es la ciudad más poblada en Africa
'''
import pandas as pd
excel = pd.ExcelFile('/Users/AriasC/Documents/ITCH/Arias/6to semestre/Proyecto Blockchain/Cursos/Inteligencia artificial/Python 3. Curso completo de Python 3. Aprende desde cero/poblacion.xlsx')

dataframe = excel.parse('Hoja 1')

print(dataframe['Ciudad más poblada'][3])

fichero_csv = pd.read_csv('/Users/AriasC/Documents/ITCH/Arias/6to semestre/Proyecto Blockchain/Cursos/Inteligencia artificial/Python 3. Curso completo de Python 3. Aprende desde cero/poblacion.csv')

#print(fichero_csv)

#print(fichero_csv['Ciudad más poblada'][1])
