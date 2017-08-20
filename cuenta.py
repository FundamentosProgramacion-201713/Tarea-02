#encoding: UTF-8

# Autor: Jose Antonio Gomez Mora, A01374459
# Descripcion: Usuario ingresa subtotal de comida. El programa calcula el IVA y propina y se los suma al subtotal para obtener el total.

# A partir de aquí escribe tu programa

subtotal= float(input("Escribe el total de la comida: "))
propina=subtotal*0.12
iva=subtotal*0.16

total=subtotal+propina+iva

print("Costo de la comida:",subtotal)
print("Propina:",propina)
print("IVA:",iva)
print("Total a pagar:",total)
