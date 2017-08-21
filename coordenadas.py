#encoding: UTF-8

# Autor: Mónica Monserrat Palacios Rodríguez, A01375137
# Descripcion: Coordenadas cartesianas a coordenadas polares.

# A partir de aquí escribe tu programa
import math

x= int(input("x: "))
y= int(input("y: "))

magn=((x*x)+(y*y))
mag_final=(magn)**.5

print("Magnitud:", mag_final)
grados= math.atan2(y,x)
grados1= math.degrees(grados)

print ("°:", grados1)
