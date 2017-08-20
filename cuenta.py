#encoding: UTF-8

# Autor: Omar Israel Galván García A01745810
# Descripcion: Calcula el 12% de propina y el 16% de IVA al costo total de una comida.


costo = int(input("Costo de su comida: "))
propina = (costo * 0.12)
iva = (costo * 0.16)
total = (costo + propina + iva)

print("Costo de la comida: ","$",costo)
print("Propina: ","$",propina)
print("IVA: ","$", iva)
print("Total a pagar: ","$",total)


