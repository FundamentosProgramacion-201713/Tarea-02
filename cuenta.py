#encoding: UTF-8

# Autor: Luis Enrique Neri Pérez, A01745995
# Descripcion: Programa que muestre el subtotal, propina, IVA y total a pagar en un restaurante

print("CUENTA")

subtotal= float(input("Ingrese el costo de su comida: "))

propina = float(0.12 * subtotal)
iva = float(0.16 * subtotal)
total = subtotal + propina + iva

print("Subtotal: $", subtotal )
print("Propina: $", propina )
print("IVA: $", iva )
print("TOTAL: $", total)

