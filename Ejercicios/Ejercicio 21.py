'''
Crear el diccionairo "frutas"
frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

Grabar esta estructura de datos "frutas" en un fichero binaro "fichero.pckl"
Ya que en un fichero de texto, solo se guardan carateres, pero no se pueden guardar
estas estructuras'''
import pickle

frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

fichero = open("fichero.pckl","wb")

pickle.dump(frutas, fichero)

fichero.close()
##################################################

abrir_fichero = open("fichero.pckl","rb")

diccionario_leido = pickle.load(abrir_fichero)

print(diccionario_leido)

abrir_fichero.close()
