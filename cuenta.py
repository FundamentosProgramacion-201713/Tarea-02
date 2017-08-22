#encoding: UTF-8

# Autor: Jordan González Bustamante, A01745993
# Descripcion: Programa que pide el total a pagar de una comida, y calcula los porcentajes a pagar de propina, marcado
#              como 12%, y el IVA, 16%, así mismo, mostrarle al usuario el precio total una vez calculado lo anterior.

# -----

tip = 0.12
iva = 0.16
subt = int(input("Ingrese el precio a pagar de su comida en números reales : "))
tip = subt * tip
iva = subt * iva
total = str(subt + tip + iva)
subt = str(subt)
tip = str(tip)
iva = str(iva)
print("--------------------------")
print(" Le programmer restaurant")
print("--------------------------")
print("Subtotal : $ " + subt)
print("Propina  : $ " + tip)
print("IVA      : $ " + iva)
print("--------------------------")
print("Total a pagar : " + total)

