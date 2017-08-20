#encoding: UTF-8

# Autor: Luis Enrique Neri Pérez, A01745995
# Descripcion: Programa que solicite la velocidad de un auto para determinar la distancia a 6 y 10 km: y determine el tiempo que tardará en recorrer en 500 km

print("RAPIDÓMETRO AUTOMOVILÍSTICO")
velocidadAuto= int(input("Ingrese la velocidad actual de su automovil en Km/H: "))

distanciaAuto6 = velocidadAuto * 6
distanciaAuto10 = velocidadAuto * 10
tiempo500 = 500 / velocidadAuto

print("VELOCIDAD ACTUAL:",velocidadAuto,"Km/H")
print("Distancia recorrida en 6 hrs:", distanciaAuto6, "Km")
print("Distancia recorrida en 10 hrs:", distanciaAuto10, "Km")
print("Tiempo en recorrer 500 Km:", tiempo500, "Hrs")

