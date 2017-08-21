#encoding: UTF-8

# Autor: Natalia Meraz Tostado, A01745008
# Descripcion: Desarrollar un programa que lea la cuenta de la comida e imprima la propina, IVA y total a pagar

# A partir de aquí escribe tu programa

subtotal = input("Costo de su comida: ")
subtotal = float(subtotal)

propina = subtotal * .12
iva = subtotal * .16
total = subtotal + propina + iva

print("Costo de su comida: $",subtotal)
print("Propina: $",propina)
print("IVA: $",iva)
print("Total a pagar: $",total)

