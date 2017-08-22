# Autor: Roberto Téllez Perezyera, A01374866
"""Este programa convierte coordenadas cartesianas dadas por el usuario a coordenadas polares. Muestra al usuario
el valor de la magnitud y el valor del ángulo en grados."""
import math

strCoordX = input("Teclee la coordenada X: ")
strCoordY = input("Teclee la coordenada Y: ")

coordX = float(strCoordX)
coordY = float(strCoordY)

magnitud = math.sqrt(coordX**2 + coordY**2)
anguloRad = math.atan2(coordY, coordX)
anguloGrados = (anguloRad * 180) / math.pi

print ("Magnitud: ", magnitud)
print ("Ángulo: ", anguloGrados, "grados.")