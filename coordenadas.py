#encoding: UTF-8

# Autor: Dora Gabriela Lizarraga Gonzalez, A01229599
# Descripcion: Convertir coordenadas cartesianas a polares

from math import *
catAdyacente = int(input('Coloca el valor de x: '))
catOpuesto = int(input('Coloca el valor de y: '))
magnitud = (((catAdyacente**2)+(catOpuesto**2))**(1/2))
anguloR = atan2(catOpuesto,catAdyacente)
anguloG = (anguloR*180)/pi
print('La magnitud "r" es: ', magnitud)
print('El angulo es de: ', anguloG,'º')