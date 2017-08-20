#encoding: UTF-8

# Autor: Angel Ramírez Martínez, A01273759
# Descripcion: Calcula el costo total de la comida de un restaurante en subtotal, propina, IVA y el total a pagar.

# A partir de aquí escribe tu programa
costo_comida = int( input('¿Cual es el costo de la comida? '))
subtotal = costo_comida
propina = costo_comida*0.12
iva = costo_comida*0.16
total = subtotal + propina + iva

print('El costo de la comida es:', subtotal)
print('La propina es de:', propina)
print('El IVA es de:', iva)
print('El total de la compra es de:', total)