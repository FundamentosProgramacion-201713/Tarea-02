#encoding: UTF-8

# Autor: Gabriela Mariel Vargas Franco, A01745775
# Descripcion: Calcular el costo total de una comida en un restaurante.

# A partir de aquí escribe tu programa
strCosto=input("Costo comida: ")
costo=int(strCosto)
#1.

propina=costo * 0.12

#2.
iva=costo * 0.16

#3.
totalPagar=costo+propina+iva
print("Subtotal: ", costo)
print("Propina: ", propina)
print("IVA: ", iva)
print("Total a pagar: ", totalPagar)

