#encoding: UTF-8

# Autor: Ana María López Soto, A01746134
# Descripcion: Calcular magnitud r y valor del ángulO

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

from math import *
r = (x**2 + y**2)**0.5
angulo = degrees(atan2(y,x))

print("X:", x)
print("Y:", y)
print("Magnitud", r)
print("Ángulo:",angulo)