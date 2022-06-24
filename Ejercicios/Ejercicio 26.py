'''
A partir de la lista "numeros" que contiene números del 1 al 10, obtener
mediante "filter" una lista denominada "pares" con los números pares de la lista "numeros"
'''

numeros = [1,2,3,4,5,6,7,8,9,10]

def par(numero):
    if(numero % 2) == 0:
        return True
    else:
        return False


resultado = filter(par, numeros)

pares = list(resultado)
