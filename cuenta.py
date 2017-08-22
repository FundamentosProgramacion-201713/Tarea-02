#encoding: UTF-8

# Autor: Luis Alfonso Alcántara López Ortega, A01374785
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# A partir de aquí escribe tu programa

costo = float(input("Costo de su comida: "))
propina = costo * 0.12
iva = costo * 0.16
costoTotal = costo + propina + iva

print("Propina: ", round(propina, 2), sep="$")
print("IVA: ", round(iva, 2), sep="$")
print("Total a pagar: ", round(costoTotal, 2), sep="$")

