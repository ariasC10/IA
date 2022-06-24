'''
1. Crea una variable "minimo" con el valor 20
2. Crea una variable "maximo" con el valor 500
3. Recoge un valor del teclado y almacénalo en la variable "dato"
4. Convierte la variable "dato" en un número y almacénalo en la variable "numero"
5. Si el "numero" es menor que el valor de "minimo", mostrar el texto "Valor bajo"
6. Si el "numero" es mayor que el valor "maximo", mostrar el texto "Valor alto"
7. Si el "numero está entre el valor "minimo" y "maximo", mostrar "Valor medio"
'''

minimo = 20
maximo = 500

print("Ingrese un número")
dato = input()

numero = int(dato)

if(numero < minimo):
    print("Valor bajo")
elif (numero > maximo):
    print("Valor alto")
else:
    print("Valor medio")


#Otra resolución
'''
if(numero < minimo):
    print("Valor bajo")

if(numero < maximo):
    print("Valor alto")

if(numero < minimo) and (numero > alto):
    print("Valor medio")
'''
