'''
1. Crear una variable "inicio" con el valor 1
2. Crear una variable "fin" con el valor 6
3. Hacer un bucle while que muestre tantas filas como valores haya entre "inicio" y "fin"
4. En cada iteración del bucle mostrar el texto "Esta es la fila " + número de fila en la que está
'''

inicio = 1
fin = 6
fila = 1

while(fila in range(inicio, fin)):
    print("Esta es la fila {}".format(fila))
    fila += 1
