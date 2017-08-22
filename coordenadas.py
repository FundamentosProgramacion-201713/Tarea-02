#encoding: UTF-8

# Autor: Nazdira Abigail Cerda deL Prado, A01375428
# Descripcion: Convierte de coordenadas cartesianas a coordenadas polares y calcula la magnitud de "r" preguntando al usuario los valores de "x" y "y"

# A partir de aquí escribe tu programa

x1=int(input("Insertar valor de x:"))
y1=int(input("Insertar valor de y:"))

import math
angulo= math.atan2(y1,x1)
magnitud=((x1**2)+(y1**2))**0.5
anguloc=(angulo*180)/3.1416

print("Magnitud:")
print(magnitud)
print("Angulo:")
print(anguloc)