#encoding: UTF-8

# Autor: Irving Fuentes Aguilera, A01745759
# Descripcion: Programa que calcula el total de la cuenta de una comida.
# A partir de aquí escribe tu programa

subtotal= float(input("Ingresar subtotal de la comida: "))
propina= subtotal * 0.12
iva= subtotal * 0.16
total= subtotal + iva + propina

print("subtotal: ", subtotal)
print("propina: ", propina)
print("iva:", iva)
print("total: ", total)
