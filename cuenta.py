#encoding: UTF-8

# Autor: Jaime Orlando López Ramos
# Descripcion: Un programa en el cual el usuario introduzca el precio de su consumo para poder calcular el IVA, la propina
# y el precio total a pagar

# A partir de aquí escribe tu programa
c1= input("Introduzca el total de su consumo: ")
c= int(c1)
p= c*0.12
i= c*0.16
t= c + p +i
print("Su subtotal fue de:", c, "pesos. La propina fue de:", p, "pesos. Su IVA de:", i, "pesos" )
print("su gran total fue de:", t, "pesos")