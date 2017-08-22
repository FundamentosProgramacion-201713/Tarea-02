#encoding: UTF-8

# Autor: David Ramrírez Ríos, A01338802
# Descripcion: Calcular el costo total de una comida.

# A partir de aquí escribe tu programa

costoDeComida = float (input("Teclea el total de tu comida: "))
propina = costoDeComida * .12
iva = costoDeComida * .16
total = costoDeComida + propina + iva

print("Costo de su comida: ", costoDeComida)
print("Propina: $", propina)
print("I.V.A.: $", iva)

print("Total a pagar: $", total)

