'''
Crear una lista de 1000 valores aleatorios que sigan una distribucion normal
Crear un histograma mediante matpoltlib con la lista de valores
Crear un diagrama de caja (donde se acumula el 50% de los valores) mediante seaborn
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

lista_valores = np.random.randn(1000)

plt.hist(lista_valores)

sns.boxplot(lista_valores)
