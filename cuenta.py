#encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez, A01375560
# Descripcion: Este programa calcula el total a pagar por una comida en un restaurante, incluyendo propina e impuestos.

# A partir de aquí escribe tu programa
#1
comida = int(input("Cuál ha sido el total de tu consumo? "))
#2
subtotal = comida
propina = comida*0.12
impuesto = comida*0.16
#3
total = comida + propina + impuesto
#4
print ("Subtotal de su comida: $", str(subtotal))
print ("Propina: $", str(propina))
print ("Impuestos: $", str(impuesto))
print ("Total a pagar: $", str(total))
