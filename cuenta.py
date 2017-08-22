#encoding: UTF-8

# Autor: Juan Sebastián Lozano Derbez, A01374452
# Descripcion: Calcular el total de la cuenta contando la propina y el IVA.

# A partir de aquí escribe tu programa

nototal = float(input("Costo de la comida: "))

propina = nototal * 12/100
IVA = nototal * 16/100

total = nototal + propina + IVA

print("Propina", propina)
print("IVA", IVA)
print("Total a pagar:", total)