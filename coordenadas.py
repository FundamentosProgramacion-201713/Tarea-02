
# Autor: Saul Rodrigo Toral Luna     Matricula: A01745007
# Descripción: El programa convertirá de coordenadas cartesianas a polares

#1.-  Ingresar valores para coordenadas (x,y)
import math

x = input("Ingresa un valor para x: ")
y = input("Ingresa un valor para y: ")

#2.- Calcular el valor de la magnitud de "r"
#      Usando el teorema de pitagoras c= (x^2 + y^2)^1/2

r = ((int(x)**2) + int(y)**2)**0.5

#3.- Calcular el valor del angulo en grados.
#      Usando arctan(y/x)

g = math.atan2(float(y),float(x))

#4.- Al usar arctan, python regressa valores de -pi a pi
#     Por lo tanto para convertir a grados se multiplica por 180/pi

grados = (g) * (180/math.pi)

#5.- Imprimir la magnitud de r y los grados

print("La magnitud de r es de: ", r)
print("Los grados son: ", grados)
