'''
Crear la funcion "operacion" que dados 3 números, divida el primer número entre la resta de los otros
dos números

Utilizar la función creada con los números 5,4,2
Utilizar la función creada con los números 6,3,3

Utilizar el bloque try ... except para controlar cualquier posible error'''

def operacion(n1,n2,n3):
    result = n1 / (n2 - n3)
    return result

n1 = 6
n2 = 3
n3 = 3


try:
    resultado = operacion(n1,n2,n3)
    print(resultado)
    
except:
    print("Error. Cambie los ultimos dos números")
