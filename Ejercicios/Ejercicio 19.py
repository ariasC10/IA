'''
Crear un modulo "modulo1.py"
Añadir la clase "Coche" creada en un ejercicio al modulo "modulo1"
Añadir la función lambda "media" creada en un ejercicio anterior al modulo "modulo1"

Crear un programa en Python "programa1.py" (Ejercicio 19)
Importar el modulo "modulo1" antes creado
Crear un objeto "coche1" al instanciar la clase "Coche"
Mediante print mostrar las caracteristicas del coche
Calcular la media de 3 notas y mostrar el resultado con print

Ejecutar el programa "programa.py" y ver el resultado
'''
import modulo1


coche1 = modulo1.Coche("Opel", "rojo", "gasolina", "1.6")

print(coche1.mostrar_caracteristicas())

media = modulo1.media(5,5,5)
print("Nota media: {}".format(media))
