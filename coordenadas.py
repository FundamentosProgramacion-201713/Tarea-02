#Autor: Luis Alfonso Alcántara López Ortega
from math import *

x = float(input("x: "))
y = float(input("y: "))

magnitud = sqrt(x**2 + y**2)
angulo = (atan2(y,x))* 180 / 3.14

print("Magnitud: ", magnitud)
print("Ángulo: ", angulo)