'''
A partir de una lista de números del 1 al 10, obtener una nueva lista con todos
los elementos incrementados en 10 unidades
'''

numeros = [1,2,3,4,5,6,7,8,9,10]

def incrementar(numero):
    resultado = numero + 10
    return resultado

resultado = map(incrementar, numeros)

numeros2 = list(resultado)

print(numeros2)
