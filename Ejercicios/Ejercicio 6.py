'''
1. Imprime por pantalla el texto "Introduce el primer número"
2. Crear la variable "dato1" con el primer valor introducido en el paso anterior
3. Imprime por pantalla el texto "Introduce el segundo número"
4. Crear la variable "dato2" con el segundo valor introducido en el paso anterior
5. Convertir la variable "dato1" en una variable númerica denominada "numero1"
6. Convertir la variable "dato2" en una variable númerica denominada "numero2"
7. Crear la variable "suma" con la suma de "numero1 y "numero2"
8. Convertir la variable "suma" en una variable de texto denominada "strSuma"
9. Crear la variable "resultado" con la concatenacion de "La suma es " y "strSuma"
10. Imprimir el valor de "resultado"
'''

print("Introduce el primer número")
dato1 = input()

print("Introduce el segundo número")
dato2 = input()

numero1 = int(dato1)
numero2 = int(dato2)

suma = numero1 + numero2

strSuma = str(suma)

resultado = "La suma es " + strSuma

print(resultado)
