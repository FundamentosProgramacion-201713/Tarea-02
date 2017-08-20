#encoding: UTF-8

# Autor: Luis Fernando Figueroa Rendon, A01746139
# Descripcion: Pedir el costo de la comida para sacar la propina, el IVA y el total.

# A partir de aquí escribe tu programa

costo= input("Costo de la comida: ")

costo= float(costo)

propina= costo*0.12

iva= costo*0.16

total= costo + propina + iva

print("Propina: $", propina)

print("IVA: $", iva)

print("Total a pagar: $", total)
