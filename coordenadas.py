#encoding: UTF-8

# Autor: Raul Ortiz Mateos, A01375407
# Descripcion: Tenemos que encontrar la magnitud y el angulo, pidiendo x y y

# A partir de aquí escribe tu programa

from math import atan2,pi


x = float( input("¿Cual es el valor de x? "))
y = float (input("¿Cual es el valor de y? "))

magnitud = (x**2 + y**2)**0.5
angulo = atan2(y,x)*(180/pi)

print( "el valor de magnitud r :", magnitud)
print( "el valor del angulo es",angulo,"grados")