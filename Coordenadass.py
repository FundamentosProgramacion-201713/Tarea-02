#Autor: Luis Fernando Figueroa Rendon, A01746139

#Descripcion: Mediante la coordenadas "x" y "y" sacar la magnitud de "r" y sus grados.

x= input("Valor de x: ")

y= input("Valor de y: ")

x= float(x)

y= float(y)

import math

#Sacar la magnitud de "r" mediante el Teorema de Pitagoras
# hipotenusa(r)**2 = cateto opuesto(y)**2 + cateto adyacente(x)**2

r= (y**2 + x**2)**0.5

#Sacar los grados con atan2(y,x), dichos valores tienen rango de -pi a pi.

g= math.atan2 (y , x)

# Convertir los radianes a grados.

grados= (180) * (g/math.pi)

print("Magnitud de r:", r)

print("Grados:", grados, "°")
