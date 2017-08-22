#encoding: UTF-8

# Autor: Leonardo Castillejos Vite A01375332
# Descripcion: Lee el costo de una comida y calcula el IVA, la propina y el total

# A partir de aquí escribe tu programa

costo = int(input("Escriba el costo de su comida "))
propina = costo * .12
IVA = costo * .16
total = costo + IVA + propina

print("Subtotal: ", costo, sep="$")
print("Propina: ", propina, sep="$")
print("IVA: ", IVA, sep="$")
print("Costo total: ", total, sep="$")

