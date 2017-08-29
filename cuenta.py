#encoding: UTF-8

# Autor: Javier León Alcántara , A01745532
# Descripcion: Calcula el costo total de una comida en un restaurante.

subtotal = float(input("Escriba el total de la comida"))

propina = (subtotal*0.12)
iva = (subtotal*0.16)
total = subtotal+propina+iva

print("Costo de su comida :" , subtotal)
print("Propina :", propina)
print("iva :", iva)
print("Total a pagar : ", total)


