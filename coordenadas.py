#encoding: UTF-8

# Autor: Javier León Alcántara , A01745532
# Descripcion: Convierte de coordenadas cartesianas a coordenadas polares.

from math import *

x = float(input("Escriba el valor de x"))
y = float(input("Escriba el valor de y"))

r = sqrt(x**2 + y**2)
angulorad = atan2(y,x)
angulo = angulorad*(180/pi)
print("Magnitud :" ,r )
print("Angulo :", angulo, "grados")
