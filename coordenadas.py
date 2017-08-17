#encoding: UTF-8

# Autor: Luis Miguel Baqueiro Vallejo, A01745997
# Descripcion: Problema 5
import math

x = int(input("Valor de x: "))
y = int(input("Valor de y: "))
magnitud = (((x**2) + (y**2))**(1/2))
if x > 0 and y > 0:
    x = math.fabs(x)
    y = math.fabs(y)
    angulo = (math.atan(y/x)) * (180/math.pi)
if x > 0 and y < 0:
    x = math.fabs(x)
    y = math.fabs(y)
    angulo = ((math.atan(y / x)) * (180 / math.pi)) + 270
if x < 0 and y < 0:
    x = math.fabs(x)
    y = math.fabs(y)
    angulo = ((math.atan(y / x)) * (180 / math.pi)) + 180
if x < 0 and y > 0:
    x = math.fabs(x)
    y = math.fabs(y)
    angulo = ((math.atan(y / x)) * (180 / math.pi)) + 90
print("Magnitud: ",magnitud)
print("Angulo: ", angulo)
