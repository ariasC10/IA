'''
-Sumar tus 2 cartas para que sumen lo máximo posible sin pasarse de 21
-Si te pasas de 21, pierdes
-Las cartas j,q,k valen 10
-La carta '1' as puede valer 1 o 11 (puedes elegit el que más te convenga en cada caso).
-El crupier te da una carta levantada (se puede ver el valor) y él se coge 2 cargas (levanta 1 y la otra
queda cubierta). Después te da una segunda carta levantada (se ve el valor).
-Es decir tu tienes 2 cartas lavantadas (se ve el valor) y el crupier tiene 1 carta levantada y otra carta
tapada (no se ve el valor)
-Luego te pregunta si quieres más cartas. Si le dices que 'si', entonces el crupier te da otra carga
descubierta, y te vuelve a preguntar si quieres más cartas. Es decir te sigue dando cartas hast que le dices
que 'no' o hasta que te has pasado de 21 y ya has perdido
-Cuando ya no quieres más cartas, entonces el crupier levanta la carta que tenia tapada. Si la suma de sus
cartas es menor que 17 (16 o menos) tendrá la obligación de escoger una tercera carta. Si con esta cara
suma 17 o más, entonces tendrá que escoger más cartas para intentar ganarte o empatar (es decir, que sus cartas
sumen un número igual o mayor que la suma de tus cartas)
-Ganas si la suma de tus cartas es in valor menor o igual a 21, y además la suma de tus cartas es mayor que la
suma de las cartas del crupier (si tampoco se ha pasado de 21)
-Si el crupier se ha pasado de 21, tu ganas
-Si tu te pasas de 21, el crupier gana
-Si la suma de tus cartas es igual a la suma de las cartas del crupier, entonces hay empate
-Recuerda que la carta con número '1' o 'as', puede tener un valor de '1' u '11' según te convenga
'''
import random
import replit

def generar_carta():
    cartas=[11,2,3,4,5,6,7,8,9,10,10,10]
    carta = random.choice(cartas)
    return carta

def calcular_suma(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def mostrar_ganador(marcador_usuario,marcador_ordenador):
    if marcador_usuario == marcador_ordenador:
        texto = "Empate"
    elif marcador_ordenador == 0:
        texto = "Has perdido. El ordenador tiene 21 - Blackjack"
    elif marcador_usuario == 0:
        texto = "Has ganado. Tienes 21 - Blackjack"
    elif marcador_usuario > 21:
        texto = "Has perdido, la suma de tus cartas es mayor a 21"
    elif marcador_ordenador > 21:
        texto = "Has ganado, la suma de las cartas del ordenador es mayor a 21"
    elif marcador_usuario > marcador_ordenador:
        texto = "Has ganado"
    else:
        texto = "Has perdido"
    return texto

def jugar():
    print("Estamos jugando...")

    cartas_usuario = []
    cartas_ordenador=[]
    finalizado = False

    for valor in range(2):
        carta = generar_carta()
        cartas_usuario.append(carta)
        
        carta_ordenador = generar_carta()
        cartas_ordenador.append(carta_ordenador)

                
    while not finalizado:
        marcador_usuario = calcular_suma(cartas_usuario)
        marcador_ordenador = calcular_suma(cartas_ordenador)
        
        print(f"Cartas del usuario = {cartas_usuario}, marcador = {marcador_usuario}")
        print(f"Cartas del ordenador = {cartas_ordenador}, marcador = {marcador_ordenador}")

        if marcador_usuario == 0 or marcador_ordenador == 0 or marcador_usuario > 21:
            finalizado = True
        else:
            mas_cartas = input("¿Quieres más cartas?. Escribe 'si' o 'no': ")
            if mas_cartas == 'si':
                cartas_usuario.append(carta)
            else:
                finalizado = True
    

    while marcador_ordenador != 0 and marcador_ordenador < 17:
        carta_ordenador = generar_carta()
        cartas_ordenador.append(carta)
        marcador_ordenador = calcular_suma(cartas_ordenador)


    print(f"Cartas del usuario = {cartas_usuario}, marcador = {marcador_usuario}")
    print(f"Cartas del ordenador = {cartas_ordenador}, marcador = {marcador_ordenador}")

    texto = mostrar_ganador(marcador_usuario, marcador_ordenador)
    print(texto)

#Principio del programa
while input("¿Quieres jugar al Blackjack?. Escribe 'si' o 'no': ") == 'si':
    
    jugar()


