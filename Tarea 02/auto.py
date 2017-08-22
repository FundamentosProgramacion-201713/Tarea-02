#encoding: UTF-8

# Autor: Pedro Cortés Soberanes A01374919
# Descripcion: Este programa calcula la distancia y tiempo que recorre un auto

v = int(input("Escribe en km/h la velocidad del auto:  "))

d1 = v*6
d2 = v*10
t1 = 500/v

print ("- Velocidad del auto en km/h: ", v)
print ("- Distancia recorrida en 6 hrs: ", d1)
print ("- Distancia recorrida en 10 hrs: ", d2)
print ("- Tiempo para recorrer 500 km: ",t1)
