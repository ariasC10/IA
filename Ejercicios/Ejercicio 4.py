'''
1. Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
2. Crear una variable "longitud" que contiene la logitud de la variable "cadena"
3. Crear una variable "strlongitud" que tenga el valor de "longitud" pero convertida
a cadena de caracteres o string
4. Crear una variable "mayusculas" que contenga la variable "cadena" en mayúsculas
5. Crear una variable "resultado" que concatene "mayúsculas" con el texto "tiene longitud de "
y "strlongitud"
'''

cadena = "Esto es un texto de ejemplo"

longitud = len(cadena)

strLongitud = str(longitud)

mayusculas = cadena.upper()

resultado = mayusculas + " tiene una longitud de " + strLongitud
