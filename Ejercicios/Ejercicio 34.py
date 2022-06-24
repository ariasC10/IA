'''
Obtener la tabla de países de la página 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'
Limpiar los datos lo necesario para que los nombres de las columnas sean correctos
'''

import pandas as pd
url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'

datos = pd.io.html.read_html(url)

paises = datos[0]

paises = paises.rename(columns=dict(paises.loc[0]))

paises = paises.drop(0)
