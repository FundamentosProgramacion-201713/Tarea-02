#encoding: UTF-8

# Autor: Jose Antonio Vazquez Gabian, A01746585
# Descripcion: programa que calcula el porcentaje de hombres y mujeres inscritos en una clase

# A partir de aquí escribe tu programa

import math

x= int(input("Valor de coordenada absisa: "))
y= int(input("Vaor de la coordenada ordenada: "))
math.atan2(y, x)
r=((x**2 + y**2)**0.5)
g= math.atan2(float(y),float(x))
angulo= g*(180/3.1416)
print("Valor de Magnitud",r)
print("Valor de angulo", angulo)
