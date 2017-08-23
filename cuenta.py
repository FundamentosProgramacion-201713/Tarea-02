#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: calcula el costo total de una comida en un restaurante icluyendo el total de lo que comiste, ms la propina y el IVA

str_tcomida = input("Costo de su comida:")
total_comida = int(str_tcomida)

prop = total_comida * 0.12
iva = total_comida * 0.16
total = (total_comida+prop+iva)

print("Costo de su comida:", "$", total_comida)
print("Propina:", "$", prop)
print("IVA:", "$", iva)
print("Total a pagar:", "$", total)
