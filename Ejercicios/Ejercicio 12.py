'''
1. Crear una variable "conjunto" que sea un conjunto de los valores 1,2,3,4 y 5
2. Mostrar el valor de la variable "conjunto"
3. Añadir los números 6,7,8 y 9 a la variable "conjunto"
4. Mostrar ahora el valor de la variable "conjunto"
5. Eliminar el numero 9 de la variable "conjunto"
6. Mostrar ahora el valor de la variable "conjunto"
7. Verificar que tipo de dato es la variable "conjunto" mediante type()
'''

conjunto = {1,2,3,4,5}

print(conjunto)

conjunto.add(6)
conjunto.add(7)
conjunto.add(8)
conjunto.add(9)

print(conjunto)

conjunto.remove(9)

print(conjunto)

print(type(conjunto))
