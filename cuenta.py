#encoding: UTF-8

# Autor: Jose Antonio Vazquez Gabian, A01746585
# Descripcion: programa que calcula el costo total de una comida en un restaurant.

# A partir de aquí escribe tu programa

subtotal= float(input("Costo de comida: "))
propina=subtotal*0.12
iva=subtotal*0.16
total=subtotal+iva+propina

print("Subtotal", subtotal)
print("Iva", iva)
print("Propina", propina)
print("Total a pagar", total)
