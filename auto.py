#encoding: UTF-8

# Autor: Roberto Téllez Perezyera, A01374866
### Descripcion: Este programa calcula la distancia recorrida por un auto a la velocidad que indique el usuario, así
# como el tiempo requerido para que se recorran 500 kilómetros.

# A partir de aquí escribe tu programa

strVel = input ("Introduce con números la velocidad del auto: ")
vel = float(strVel)
dist6Hrs = vel * 6
dist10Hrs = vel * 10
timeFor500 = (500 / vel)

print ("Distancia recorrida en 6 horas: ", dist6Hrs, "km.")
print ("Distancia recorrida en 10 horas: ", dist10Hrs, "km.")
print ("Para recorrer 500 km, el auto tardará", timeFor500, "horas.")