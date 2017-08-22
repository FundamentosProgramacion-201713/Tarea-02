# Autor: Genaro Ortiz Durán, A01375315
# Descripcion: Convertir coordenadas cartesianas a coordenadas polares.
from math import atan2, pi
strA= input("¿Cual la coordenada x?:")
a= int(strA)

strB= input("¿Cual es la coordenada y?:")
b= int(strB)

r=((a**2+b**2)**0.5)
angulo= atan2(b,a)*(180/pi)

print("R es:", r)
print("El angulo es:",angulo)