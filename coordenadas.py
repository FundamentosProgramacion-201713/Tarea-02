#encoding: UTF-8

# Autor: Jordan González Bustamante, A01745993
# Descripcion: Programa que imprime la magnitud de la resultante, y el valor de ángulo en grados segun las coordenadas
#              capturadas por el usuario.

# -----
import math
x = float(input("Ingrese la coordenada x : "))
y = float(input("Ingrese la coordenada y : "))
h = float(math.sqrt(((x**2) + (y**2))))
r = math.degrees((math.atan2(y,x)))
x = str(x)
y = str(y)
h = str(h)
r = str(r)
print("Coordenada X : " + x)
print("Coordenada Y : " + y)
print("Magnitud     : " + h)
print("Ángulo       : " + r)



