'''
Crear el modulo "moduloficheros.py"
    Crear una clase "Fichero"
    Crear la funcion "leer_fichero" para leer un fichero de texto
    Crear la funcion "grabar_fichero" para crear un fichero de texto
    Crear la funcion "incluir_fichero" para incluir datos al final de un fichero de texto

Crear un programa "programa1" (Ejercicio 20)
    Crear el objeto "fichero" de la clase "Fichero" del modulo "moduloficheros.py"
    Utilizar el método "grabar_fichero" del objeto "fichero" para crear un nuevo fichero
    Utilizar el método "incluir_fichero" para incorporar más datos al final del fichero
    Utilizar el método "leer_fichero" para ver todo el contenido del fichero

Ejecutar el programa para observar los resultados '''

import moduloficheros

fichero = moduloficheros.Fichero

fichero.grabar_fichero()

fichero.incluir_fichero()

fichero.leer_fichero()
