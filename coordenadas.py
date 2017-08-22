#Autor: Neftalí Rodríguez MArtínez, A01375808.
#Este programa lee las coordenadas cartesianas (x,y) y entrega la margnitud (r) y el ángulo entre las dos
#coordenadas.

import math

x = float(input("Escribe el valor de x: "))
y = float(input("Escribe el valor de y: "))

magnitud = ((x ** 2)+ (y ** 2)) ** 0.5
angulo = ((math.atan2(y,x)) * 180) / math.pi

print ("La magnitud de las coordenadas cartesianas es: ", magnitud)
print ("El ángulo formado por (x,y) es: ", angulo)