#Autor: Javier Matínez Hernández A01375496
#Descripcion: se preguntara por las coordenadas cartesianas y se pasaran a polares
from math import *

x=float(input("Introduce x: "))
y=float(input("Introduce y: "))
magnitud= (x**2+y**2)**1/2
direccion= atan2(y,x)
direccion=direccion*(180.0/pi)
print("Magnitud: ", magnitud, "\nDireccion: ", direccion, "°")