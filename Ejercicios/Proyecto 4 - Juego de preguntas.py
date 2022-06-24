'''
Primero preguntamos izquierda o derecha, luego si nadar o esperar y de último
cuál puerta abrir rojo, azul o verde
Si adivina correctamente pasa a la siguiente pregunta
'''
print("Juego de preguntas")
respuesta1 = input('¿Quieres ir a la izquierda o a la derecha?. Ecribe "izquierda" o "derecha" ').lower()

if respuesta1 == 'izquierda':
    print("Te haz caído a un pozo. Siga participando")
else:
    respuesta2 = input('Bien, tienes que cruzar un río, ¿Vas nadando o esperas a que llegue un bote?. Escribe "nadar" o "esperar" ')
    respuesta2 = respuesta2.lower()
    if respuesta2 == 'nadar':
        print('Mala idea, te comieron los cocodrilos. Suerte a la próxima')
    else:
        respuesta3 = input("Has llegado a una casa con 3 puertas. Una azul, otra roja y la última verde. ¿Cuál eliges?. Escribir 'azul', 'rojo' o 'verde' ")
        respuesta3 = respuesta3.lower()
        if respuesta3 == 'rojo' or respuesta3 == 'azul':
            print("Uy, casi lo consigues, entraste a un cuarto con trampas")
        else:
            print("¡¡Que grande, haz ganado!!")
