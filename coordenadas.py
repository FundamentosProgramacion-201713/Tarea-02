#encoding: UTF-8

# Autor: Alberto López Reyes, A01745811
# Descripcion: Este programa calcula la magnitud y ángulo de un triángulo a partir de
# dos coordenadas otorgadas.

# A partir de aquí escribe tu programa

import math

intCatetoX = int(input("x: "))
intCatetoY = int(input("y: "))

fltHipotenusa = math.sqrt((float(intCatetoX))*(float(intCatetoX)) + float(intCatetoY)*float(intCatetoY))
fltAngulo = math.atan(float(intCatetoY) / float(intCatetoX))

print(str("Magnitud: " + str(fltHipotenusa)))
print(str("Angulo: " + str(math.degrees(fltAngulo))))