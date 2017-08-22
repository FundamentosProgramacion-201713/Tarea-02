#endoding: UTF-08

#Autor: Jaime Orlando López Ramos
#Descripción: Un programa que pregunta al usuario los valores x, y de un triángulo y de el valor de la hipotenusa "r"
#e imprimir el ángulo en grados

from math import atan2

x= input("Ingrese el valor de x: ")
x= int(x)
y= input("Ingrese el valor de y: ")
y= int(y)
r= ((x**2)+(y**2))**0.5
tr= atan2(y, x)
tg= tr*180/3.1416
print("La magnitud 'r' tiene un valor de:", r, "unidades y su ángulo es de:", tg, "grados")
