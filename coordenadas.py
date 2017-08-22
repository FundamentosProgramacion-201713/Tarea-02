# encoding: UTF-8

# Autor: Jose Heinz Moller Santos, A01375623
# Descripcion: Este programa te calcula los grados respecto a X y magnitud de un vector

# A partir de aquí escribe tu programa

import math

X = int(input("Dame las coordenadas en X: "))
Y = int(input("Dame las coordenadas en Y: "))

angulo = math.atan2(Y,X)

magnitud = math.sqrt(X ** 2 + Y ** 2)

# = math.asin(Y/magnitud)

print("Angulo: ", angulo)
print("Magnitud: ", magnitud)
