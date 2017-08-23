#encoding: UTF-8

# Autor: Daniel Ricardo Sahuer Balmaceda, A01375823
# Descripcion: El usuario escribe la velocidad y con esa magnitud se calcula distancias de acuerdo a un tiempo específico y tiempo con una distancia dada.

fltv = input("Escribe la velocidad del auto (km/h): ")
v = float(fltv)

d1 = v*6
d2 = v*10
t = 500/v

print ("Distancia recorrida en 6 hrs: ",d1," km")
print ("Distancia recorrida en 10 hrs: ",d2,"km")
print ("Tiempo para recorrer 500 km: ",t," hrs")
