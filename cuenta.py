#encoding: UTF-8

# Autor: Ángel Guillermo Ortiz González, A01745998
# Descripcion: Cálculo de porcentajes de propina e impuestos con base en el costo de la comida para obtener el total de la cuenta.

# A partir de aquí escribe tu programa

comida = float(input("Inserte el total de la comida: "))
propina = comida * 0.12
iva = comida * 0.16
total = comida + propina + iva

print ("Costo de su comida: $",comida, """
Propina: $""",propina, """
IVA: $""",iva, """
Total a pagar: $""",total)