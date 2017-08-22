# Autor: Joaquin Rios Corvera A01375441
#Descripción: Convertir coordenadas cartesianas a polares

import math
x = float(input("Cuál es la coordenada x?"))
y = float(input("Cuál es la coordenada y?"))

angulo = math.atan2(y,x) * 180 / math.pi
magnitud = math.sqrt(x**2 + y**2)

print("Angulo:", round(angulo,2))
print("Magnitud:", round(magnitud, 2))