'''
Crear un array con 100 números enteros aleatorios con valores comprendidos entre 0 y 500
Utilizar un diagrama de caja para representar los valores aleatorios generados
'''
import numpy as np
import seaborn as sns

datos = np.random.randint(0,500,100)

sns.boxplot(datos)
