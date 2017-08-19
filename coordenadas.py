#encoding: UTF-8

# Autor: MARIA FERNANDA TORRES VELAZQUEZ, A01746537
# Descripcion: El siguiente programa transforma coordenadas cartesianas a polares.

import math

x= int (input("Introduce el valor de la coordenada x " ))
y= int (input("Introduce el valor de la coordenada y " ))

r= (x**2 + y**2) ** 0.5
div= y/x
angr= math.atan(div)
angrad= math.degrees(angr)

print("Magnitud: ",r)
print ("Angulo: ",angrad,"grados")






