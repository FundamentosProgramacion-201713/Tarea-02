#encoding: UTF-8

# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

str_tcomida = input("Costo de su comida:")
total_comida = int(str_tcomida)

prop = total_comida * 0.12
iva = total_comida * 0.16
total = (total_comida+prop+iva)

print("Costo de su comida:", "$", total_comida)
print("Propina:", "$", prop)
print("IVA:", "$", iva)
print("Total a pagar:", "$", total)
