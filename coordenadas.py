#encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Este programa permite calcular la magnitud y la dirección de un vector a partir de las coordenadas dadas.

# A partir de aquí escribe tu programa

import math
print("Bienvenido")
print("")
print("El siguiente programa te permitira obtener la magnitud y la dirección de un vector a partir de las coordenadas x y y")
valorx=input("Introduce cuanto vale x: ")
valory=input("Introduce cuanto vale y: ")
print("")
print("El valor de la coordenada polar es: ")
angulo=(math.atan2(int(valory),int(valorx)))*60
magnitud=math.sqrt((int(valorx)**2)+(int(valory)**2))
print("Una magnitud de: ", magnitud)
print("Un angulo de: ", angulo)