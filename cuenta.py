#encoding: UTF-8

# Autor: Javier Martínez Hernández A01375496
# Descripcion: Calcular el coste total de una comida, incluyendo IVA y propina

subtotal=int(input("costo de la comida: "))
iva=subtotal*.16
prop=subtotal*.12
total= subtotal+iva+prop
print("IVA $", iva, "\nPropina $", prop, "\nTotal $",total)