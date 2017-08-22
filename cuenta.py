#encoding: UTF-8

# Autor: Jean Paul Esquivel Lobato,   A01376152
# Descripcion: Calcular el precio total que se tiene que pagar en un restaurante.

costo = float(input("Cuánto costó la comida que compraste?"))

IVA = costo * 0.16
propina = costo * 0.12
costoTotal = costo + IVA + propina


print("Tu subtotal fue de: $", costo)

print("El IVA fue: $", round(IVA, 2))

print("La propina es: $", round(propina, 2))

print("El total es: $", round(costoTotal, 2))