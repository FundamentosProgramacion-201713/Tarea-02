#encoding: UTF-8

# Autor: Genaro Ortiz Durán, A01375315
# Descripcion: Calcular el costo de una comida ya incluyendo el IVA y la propina.

strA= input("¿Cual fue el costo de la comida?:")
a= int(strA)

Propina= a*.12
IVA= a*.16

Total=(a*.12)+(a*.16)+a
print("El total de su consumo es:", Total)


