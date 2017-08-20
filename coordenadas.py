#encoding: UTF-8

# Autor: Angel Ramírez Martínez, A01273759
# Descripcion: Convierte coordenadas cartesianas a coordenadas polares

# A partir de aquí escribe tu programa
from math import atan2, pi
x = int( input('Ingresa el valor de X '))
y = int( input('Ingresa el valor de Y '))
r = (x**2 + y**2)**0.5
angulo = atan2(y,x)*(180/pi)
print('La magnitud del vector resultante es de:', r)
print('El ángulo del vector resultante es de:', angulo, 'grados')
