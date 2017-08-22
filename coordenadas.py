#encoding: UTF-8
# Autor: David Ramrírez Ríos, A01338802

# Descripción: Convertir coordenadas cartesianas a polares.


x = int (input("Teclea el valor x: "))
y = int (input("Teclea el valor y: "))

import math
angulo = math.atan2(y ,x)


magnitud = ((x**2) + (y**2))**.5

print("Magnitud = ", magnitud)
print("Angulo = ", angulo)