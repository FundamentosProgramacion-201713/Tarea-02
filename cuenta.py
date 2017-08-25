#encoding: UTF-8

# Autor: Dora Gabriela Lizarraga Gonzalez, A01229599
# Descripcion: Se calculara el costo total de una comida en un restaurante.

# A partir de aquí escribe tu programa
costoComida = int(input('Costo de su comida: '))
propinaNeto = (costoComida*.12)
impuestoNeto = (costoComida*.16)
cuentaTotal = (costoComida + propinaNeto + impuestoNeto)
print('Subtotal: $' , costoComida)
print('Propina: $' , propinaNeto)
print('I.V.A.: $' , impuestoNeto)
print('Total a pagar: $' , cuentaTotal)
