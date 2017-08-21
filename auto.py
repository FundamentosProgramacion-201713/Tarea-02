#encoding: UTF-8

# Autor: Javier Pascal Flores, A01375925
# Descripcion:. La velocidad de un auto puede calcularse con la fórmula v = d/t. (v-velocidad, d-distancia, t-tiempo).
# Elabora un algoritmo y escribe un programa que pregunte al usuario la velocidad a la que viaja un auto (km/h) y calcule e imprima lo siguiente:
#La distancia en km. que recorre en 6 hrs.
#La distancia en km. que recorre en 10 hrs.
#El tiempo en horas que requiere para recorrer 500 km

# A partir de aquí escribe tu programa
velocidad = input( "¿Cual es la velocidad del auto en kilometros por hora? ")
type(velocidad)
velocidad = int(velocidad)
tiempo=0
distancia_6=0
distancia_10=0
distancia_6=6*velocidad
distancia_10=10*velocidad
tiempo=500/velocidad
print("Distancia en km. que recorre en 6 hrs: ", distancia_6), "km"
print("Distancia en km. que recorre en 10 hrs: ", distancia_10, "km")
print("tiempo en horas que requiere para recorrer 500 km: ", tiempo,"hrs")