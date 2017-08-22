#encoding: UTF-8

# Autor: Javier Pascal Flores A01375925}

#Descripcción: Elabora un algoritmo y escribe un programa que convierta de coordenadas cartesianas a coordenadas polares. Usa la función atan2(y,x) en Python que regresa el arcotangente de y/x en el rango - a .
#El programa le pregunta al usuario el valor de x y y.
#Imprime:
#El valor de la magnitud r.
#El valor del ángulo  en grados.
#A partir de aqui empieza mi programa
import cmath
import math


x=input("Valor en x:")
y=input("Valor en y:")
x=int(x)
y=int(y)
radianes=math.atan2(y, x)
hipotenusa = y/math.sin(radianes)
grados=math.degrees(radianes)

print("La magnitud de r es: ", hipotenusa)
print("El valor del angulo es:", grados,"°")