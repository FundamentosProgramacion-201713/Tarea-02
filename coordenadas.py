#encoding: UTF-8

# Autor: Luis Daniel Rivera Salinas, A01374997
# Descripcion: Programa que convierte las coordenadas cartesianas a polares por medio de la funcion arc tan

# A partir de aquí escribe tu programa

from math import atan2,sqrt,pi

x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))

magnitud = sqrt((x**2)+(y**2))
angulo = atan2(y,x)
angulo = (angulo*(180/pi))

print ("La magnitud es: ", magnitud)
print("El angulo es: ", angulo)
