#Autor: Ernesto Ibhar Guevara Gomez              Matricula: A01746121
# Descripcion: El programa convierte de coordenadas cartesianas a polares
import math
x = int(input("Ingresa valor de x: "))
y = int(input("Ingresa valor de y: "))

r=(x**2 + y**2)** 0.5
g=math.atan2(y,x)
grados= (g) * (180/math.pi)

print("La magnitud es: ", r)
print("Angulo", grados)
