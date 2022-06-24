'''
Calculadora de propinas
Precio de la factura
Porcentaje de la propina
Personas a repartir
'''

print("Bienvenido a la calculadora de propinas")
factura = float(input("¿Cuál es el importe de tu factura? "))

propina = int(input("¿Cuál es el porcentaje de tu propina que quieres dejar? "))
personas = int(input("¿Entre cuantas personas hay que repartir la factura? "))

importe_propina = (factura * propina)/100
factura_total = factura + importe_propina

importe_por_persona = factura_total / personas

importe_redondeado = round(importe_por_persona,2)

print("El importe a pagar por pesona es de " + str(importe_redondeado))
