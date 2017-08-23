#encoding: UTF-8

# Autor: Alberto López Reyes, A01745811
# Descripcion: Este prgrama imprime la propina, el IVA y el total del costo de una comida
# a partir de un subtotal otorgado.

# A partir de aquí escribe tu programa

intSubtotal = int(input("Costo de su comida: "))

fltPropina = (float(intSubtotal) * 12) / 100
fltIVA = (float(intSubtotal) * 16) / 100
fltTotal = float(intSubtotal) + fltPropina + fltIVA

print(str("Propina: $" + str(round(fltPropina, 2))))
print(str("IVA: $" + str(round(fltIVA, 2))))
print(str("Total a pagar: $" + str(fltTotal)))
