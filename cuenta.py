#encoding: UTF-8

# Autor: Ana María López Soto, A01746134
# Descripcion: Calcular total a pagar de una comida

# A partir de aquí escribe tu programa

subtotal = int(input("Ingrese el costo de la comida: "))

propina = subtotal * .12
iva = (subtotal * .16)
totalPagar = subtotal + propina + iva

print("Costo de su comida: $",subtotal)
print("Propina: $","%.2f" % propina)
print("IVA: $","%.2f" %iva)
print("Total a Pagar: $","%.2f" %totalPagar)