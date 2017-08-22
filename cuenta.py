#encoding: UTF-8

# Autor: Nazdira Abigail Cerda del Prado, A01375428
# Descripcion: Calcula el costo de una comida en un restaurante mostrando el subtotal agregando el 12% de propina y el 16% de IVA

# A partir de aquí escribe tu programa
floatc=input("Total de la comida:")
c=int(floatc)

subt=c
prop=c*0.12
iva=c*0.16

tot=(subt+prop+iva)

print("Subtotal:")
print(subt)
print("Propina:")
print(prop)
print("IVA:")
print(iva)
print("Total a pagar:")
print(tot)

