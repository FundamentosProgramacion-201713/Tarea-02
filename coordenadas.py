#encoding: UTF-8

# Autor: Alejandro Chávez Campos, A01374974
# Descripcion: Mi programa es de dar como resultado coordenadas polares, a partir de coordenas cartesianas.


#A partir de aquí escribe tu programa
import math
coordenadaX=float(input("Dame el valor de la coordenada en x: "))
coordenadaY=float(input("Dame el valor de la coordenada en y: "))
magnitudR=(coordenadaX**2+coordenadaY**2)**(1/2)
angulo=math.atan2(coordenadaY,coordenadaX)
print ("x: ",coordenadaX)
print ("y: ",coordenadaY)
print ("Magnitud: ",magnitudR)
print ("Angulo", angulo)

