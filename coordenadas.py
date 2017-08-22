#encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez, A01375560
# Descripcion: Este programa convierte de coordenadas cartesianas a coordenadas polares

# A partir de aquí escribe tu programa
#0
import math
#1
x = int(input("Valor de x: "))
y = int(input("Valor de y: "))
#2
arctan = math.atan2(y,x)
magnitud = y / math.sin(arctan)
grados = math.degrees(arctan)
#3
print ("Magnitud:", str(magnitud))
print ("Grados:", str(grados))
