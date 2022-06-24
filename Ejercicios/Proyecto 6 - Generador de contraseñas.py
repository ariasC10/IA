#Generador de contraseñas
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['¡','!','@','#','$','%','&','/','(',')','=','¿','?','-','_','{','}']
#Preguntar por el número de letras, números y simbolos que quieres tener en la contraseña
#Generar una contraseña aleatoria mezclando letras, números y simbolos

import random

print("Bienvenidos al generador de contraseñas")
numero_letras = int(input("¿Cuántas letras? "))
numero_numeros = int(input("¿Cuántos números ?"))
numero_simbolos = int(input("¿Cuántos simbolos? "))

lista = []


for letra in range(1, numero_letras + 1):
    valor = random.choice(letras)
    lista.append(valor)

for numero in range(1, numero_numeros + 1):
    valor = random.choice(numeros)
    lista.append(valor)

for simbolo in range(1, numero_simbolos + 1):
    valor = random.choice(simbolos)
    lista.append(valor)


print(lista)

random.shuffle(lista)
print(lista)
password = ""
for caracter in lista:
    password = password + caracter

print(password)


