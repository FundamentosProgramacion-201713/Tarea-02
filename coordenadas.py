# Autor:Rodrigo Rivera Salinas, A01375000
#Descripcion:  preguntar coordenada e imprimir magnitud y angulo

x=float(input("poner x"))
y=float(input("poner y"))

import math
x_uno=math.atan2(y,x)
angulo=(x_uno*180)/(3.14)
mag=math.sqrt(x**2+y**2)

print("La magnitud es de ",mag)
print("El angulo que se forma es de: ", angulo)


#arc y dspues de ahi tan -1

#mag catetos al cuadrado y esa wea