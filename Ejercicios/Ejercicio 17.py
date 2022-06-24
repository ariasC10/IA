'''
Crear una clase "Coche" que tenga estos atributos:
marca, color, combustible y cilindrada

Crear la función "__init__" que asigna los parametros de la clase a los atributos de la clase

Crear otra función "mostrar_caracteristicas" que mediante print muestre por pantalla
las caracteristicas (o atributos) que tiene el coche

Crear un objeto "coche1" de la clase "Coche" con los atributos "Opel", "rojo", "gasolina", "1.6"

Ejecutar la función "mostrar_caracteristicas" del objeto "coche1"
'''

class Coche:
   
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada


    def mostrar_caracteristicas(self):
        print(self.marca)
        print(self.color)
        print(self.combustible)
        print(self.cilindrada)

#coche1 = Coche("Opel", "rojo", "gasolina", "1.6")

