'''
Crear una funcion "buscar" que mediante una expresion regular indique si una palabra
está en una frase

Probar la funcion "buscar" con estas frases
    texto = "Esto es una frase de pruebas para hacer busquedas"
    palabra_a_buscar = 'frase'

En caso de encontrar la palabra en la frase, indicar en que posicion empieza y en cual finaliza
'''

import re

def buscar(palabra, texto):
    resultado = re.search(palabra, texto)
    return resultado 

texto = "Esto es una frase de pruebas para hacer busquedas"
palabra = 'frase'

resultado = buscar(palabra, texto)

if(resultado):
    print("Palabra {} encontrada".format(palabra))
    inicial = resultado.start()
    final = resultado.end()
    print("Empieza en la posición {} y termina en la posición {}".format(inicial,final))
else:
    print("Palabra {} no encontrada".format(palabra))
