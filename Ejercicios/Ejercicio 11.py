'''
1. Crear una variable "tupla" que sea una tupla de los siguientes nombres: Antonio, Pedro y Maria
2. Mostrar el valor de la variable "tupla"
3. Recoger un dato por teclado y almacenarlo en la variable "dato"
4. Si el valor "dato" está dentro de los valores de la variable "tupla", mostrar "Si"
5. Si el valor "dato" no está dentro de los valores de la variable "tupla", mostrar "No"
'''

tupla = ("Antonio", "Pedro", "Maria")

print(tupla)

print("Ingrese un nombre")
dato = input()

if(dato in tupla):
    print("Si")
else:
    print("No")

#Otra solucion
'''
if(dato in tupla):
    print("Si")
elif(dato not in tupla)
    print("No")
'''
