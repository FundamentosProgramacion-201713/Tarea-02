#encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A01339478
# Descripcion: Dando x y y convertirlas a coordenadas polares

# A partir de aquí escribe tu programa

from math import atan2, pi

x = input("Coordenada en x:")
y = input("Coordenada en y:")
magnitud = (float (x) ** 2 + float (y) ** 2)**(0.5)
angulo = atan2(float(x),float(y))*(180 / pi)
print("La magnitud es:", magnitud)
print("El angulo es:", angulo)