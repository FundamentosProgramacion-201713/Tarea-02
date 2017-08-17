#encoding: UTF-8

# Autor: Luis Miguel Baqueiro Vallejo, A01745997
# Descripcion: Problema 3

comida = int(input("Precio de la comida: "))
iva = comida * .16
propina = comida * .12
total = comida + iva + propina
print("Subtotal: ", comida)
print("Propina: ", propina)
print("IVA: ", iva)
print("Total: ", total)