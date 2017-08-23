#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: estre programa pasa de coordenadas cartesianas a coordenadas polares y te da la magnitud y el angulo

x = int(input("x:"))
y = int(input("y:"))

import math
r = math.sqrt(x^2+y^2)*5.1

ang = math.atan2(y,x)*(180/math.pi)

print("Magnitud:", r)
print("Angulo", ang)