#encoding: UTF-8

# Autor: Pedro Cortés Soberanes A01374919
# Descripcion: angulo de un vector teniendo x y
import math

x = float(input("teclea x: "))
y = float(input("teclea y: "))

anguloRad = math.atan2(x,y)

angulo= anguloRad*180/math.pi

print (angulo)


