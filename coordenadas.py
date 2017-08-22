#encoding: UTF-8

# Autor: Jean Paul Esquivel Lobato
# Descripcion: Convertir coordenadas cartesianas a polares


import math
x = float(input("Cual coordenada hay x?"))
y = float(input("Cual coordenada hay y?"))

angulo = math.atan2(y,x) * 180 / math.pi
magnitud = math.sqrt(x**2 + y**2)

print("Angulo:", round(angulo,2))
print("Magnitud:", round(magnitud, 2))