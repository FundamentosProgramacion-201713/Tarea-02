#encoding: UTF-8

# Autor: Gabriela Mariel Vargas Franco, A01745775
# Descripcion: Covertir de coordenadas cartesianas a coordenadas polares.
# A partir de aquí escribe tu programa
strX=input("Coordenada en x")
x=int(strX)
strY=input("Coordena en y")
y=int(strY)
#1.
import math
magnitud=((x*x)+(y*y))**0.5
print("Magnitud= ",magnitud)
#2.
angulo=math.atan2(y,x)*(180/math.pi)
print("Angulo: ",angulo)
