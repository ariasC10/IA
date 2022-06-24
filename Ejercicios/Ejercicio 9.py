'''
1. Crear una variable "numeros" con la lista de los números del 1 al 10 (ambos incluidos)
2. Mostrar el valor de la variable "numeros"
3. Recoger un dato del teclado y almacenarlo en la variable "dato"
4. Convertir "dato" en númerico y almacenarlo en la variable "numero"
5. Si el valor de "numero" está en la lista de número, mostrar el mensaje "Sí"
6. Si el numero introducido no está en la lista de números, mostrar el mensaje "No"
'''
numeros = [1,2,3,4,5,6,7,8,9,10]

print (numeros)

print("Ingrese un número")
dato = input()

numero = int(dato)

if(numero in numeros):
    print("El valor {} se encuentra dentro de la lista".format(numero))

if(numero not in numeros):
    print("El valor {} no se encuentra dentro de la lista".format(numero))

