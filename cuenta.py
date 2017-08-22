#

# Autor: Pablo García Morales, A01745530
# Descripcion: Programa para calcular el valor de la comida con su propina, iva y el total.

subtotal= int(input("costo de su comida"))

propina= subtotal*.12
iva= (subtotal*.16)
total= (subtotal+propina+iva)
print(subtotal)
print(propina)
print(iva)
print(total)

