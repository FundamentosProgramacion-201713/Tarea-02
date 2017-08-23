#encoding: UTF-8

# Autor: Daniel Ricardo Sahuer Balmaceda, A01375823
# Descripcion: Se pregunta por x y y, después se obtiene el ángulo y la magnitud de las coordenadas en forma polar

import math

fltx = input("x: ")
x = float(fltx)

flty = input("y: ")
y = float(flty)


anguloRad = math.atan2(y,x)
anguloGrad = anguloRad*180/math.pi

r = (x**2 + y**2)**0.5

print ("Magnitud: ",r,"\nAngulo: ",anguloGrad)