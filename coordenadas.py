#encoding: UTF-8

# Autor: Aaron Tonatiuh Villanueva Guzmán, A01375987
# Descripcion: A partir de un par de coordenadas, se obtiene el ángulo y la hipotenusa del triángulo resultante.

# A partir de aquí escribe tu programa
import math
x=float(input("Ingrese la coordenada X"))
y=float(input("Ingrese la coordenada Y"))
hipotenusa=((x**2)+(y**2))**.5
angulo= (math.atan2(x,y))*(180/math.pi)
print("La magnitud de la hipotenusa es de",hipotenusa,"unidades")
print("El ángulo es de:",angulo,"grados")
