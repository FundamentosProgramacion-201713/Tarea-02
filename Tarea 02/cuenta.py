#encoding: UTF-8

# Autor: Pedro Cortés Soberanes A01374919
# Descripcion: Este programa calcula el iva y propina de tu comida más el total

cc = int(input("Teclea el costo de tu comida en pesos:  "))
p= cc*.12
iva=cc*.16
total= cc+p+iva

print("- Costo de su comida: $",cc)
print("- Propina: $",p)
print("- IVA: $",iva)
print("- TOTAL A PAGAR: $", total)


