'''
Crear una base de datos "basededatos.db"
Crear una tabla "productos" con 3 campos
    id: Identificador del producto tipo númerico
    nombre: Nombre del producto de tipo texto
    precio: Precio del producto de tipo númerico

Insertar 3 productos en la tabla "productos"
    1, "Impresora", 300
    2, "Raton", 20
    3,"Ordenador", 600

Consultar los productos de la tabla "productos"
Cerrar la base de datos "basededatos.db"
'''

import sqlite3 

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE Productos (id INTEGER, nombre TEXT, precio INTEGER)")

#conexion.commit()

lista_productos = [(1, "Impresora", 300),
                   (2, "Raton", 20),
                   (3,"Ordenador", 600)]

cursor.executemany("INSERT INTO Productos VALUES(?,?,?)", lista_productos)

conexion.commit()

cursor.execute("SELECT * FROM Productos")
productos_seleccionados = cursor.fetchall()

for producto in productos_seleccionados:
    print(producto)

conexion.close()
