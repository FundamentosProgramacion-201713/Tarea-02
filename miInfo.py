#encoding: UTF-8

# Autor: Siham El Khoury Caviedes, A01374764
# Descripcion: Cálculo del costo total de una comida en un restaurante.

# A partir de aquí escribe tu programa:
subtotal = float(input("Indique el costo de su comida: "))
propina = subtotal * 0.12
iva = subtotal * 0.16
total = subtotal + propina + iva
print ("Subtotal: $", subtotal)
print ("Propina: $", propina)
print ("IVA: $", iva)
print ("Total a pagar: $", total)
