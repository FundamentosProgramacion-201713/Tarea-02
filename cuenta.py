#encoding: UTF-8

# Autor: Joaquin Rios Corvera A01375441
# Descripcion: Calcular el precio total que se tiene que pagar en un restaurante.

# A partir de aquí escribe tu programa

costo = float(input("Cuánto costó tu comida?"))

IVA = costo * 0.16
propina = costo * 0.12
costoTotal = costo + IVA + propina

print("Tu subtotal es: $", costo)
print("IVA: $", round(IVA,2))
print("Propina: $", round (propina,2))
print("Tu total es: $", round (costoTotal,2))
