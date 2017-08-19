#encoding: UTF-8

# Autor: Carlos Pano Hernández, A01066264
# Descripcion: COnvertidor de coordenadas cartesianas a coordenadas polares.
# A partir de aquí escribe tu programa

import math

#Introducir "x" y "y"
valorX = input("x:")
valorX = int(valorX)

valorY = input("y:")
valorY = int(valorY)

#Angulo
anguloEnRadianes = math.atan2(valorY,valorX)
angulo = (anguloEnRadianes*180)/3.1416

#Magnitud
magnitud = ((valorX*valorX)+(valorY*valorY))**0.5

#Imprimir resultados
print ("----------------------")
print ("Magnitud:", magnitud)
print ("ángulo:", angulo)