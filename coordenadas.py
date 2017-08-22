#encoding: UTF-8

# Autor: Juan Sebastián Lozano Derbez, A01374452
# Descripcion: Pasar cooredenadas cartesianas a polares.

# A partir de aquí escribe tu programa

print("----Convertidor de coordenadas cartesianas a polares 1.0----")

x = float(input("Valor de X:"))
y = float(input("Valor de Y:"))

mag = (x**2 + y**2) ** (1/2)

import math
ang = math.degrees(math.atan2(y,x))

print("Magnitud:", mag)
print("Ángulo:", ang)