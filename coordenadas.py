#encoding: UTF-8

# Autor: Luis Enrique Neri Pérez, A01745995
# Descripcion: PROGRAMA QUE DETERMINE LA MAGNITUD Y ÁNGULO DE LAS COORDENADAS X, Y
import math

print("CONVERTIDOR DE COORDENADAS")
x = float(input("Eje X: "))
y = float(input("Eje Y: "))


radianes = math.atan2(y,x)
grados = radianes * 180 / math.pi
magnitud = (x**2+y**2)**0.5

print("MAGNITUD", magnitud)
print("GRADOS:",grados)
