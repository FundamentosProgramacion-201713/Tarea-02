#encoding: UTF-8

# Autor: Viviana Osorio Nieto, A01374461 
# Descripcion: Calcular el total de una cuenta con iva y propina. 

st = int(input("cuanto es el total de la comida?"))

p = st * 0.12 

IVA = st * 0.16

T = st + p + IVA

print ("el subtotal es: ", st )
print ("la propina es: ", p)
print ("el IVA es: ", IVA)
print ("l total es: ", T)

