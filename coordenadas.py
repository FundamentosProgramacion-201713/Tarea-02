#encoding: UTF-8

# Autor: Natalia Meraz Tostado, A01745008
# Descripcion: Desarrollar un programa que lea la cuenta de la comida e imprima la propina, IVA y total a pagar

# A partir de aquí escribe tu programa

import math


x = input("x: ")
x = int(x)
y = input("y: ")
y = int(y)
math.atan2(y, x)

magnitud = ( ((x**2)+(y**2)) **.5)
angulo =  (math.atan2(y, x))*180 /3.1416

print("Magnitud: ", magnitud)
print("Angulo: ", angulo)