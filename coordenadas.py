#Autor: Irving Fuentes Aguilera
#Programa que transforma coordenadas cartesianas a polares

from math import *

x=int(input("Insertar valor de x: "))
y=int(input("Insertar valor de y: "))

magnitud=sqrt(x**2+y**2)
angulo=atan2(y,x)
angulo=angulo*(180/pi)

print("r= ",magnitud)
print("Ángulo= ", angulo)
