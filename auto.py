#encoding: UTF-8

# Autor:Rodrigo Rivera Salinas, A01375000
#  Descripcion: Calcular velocidad a partir de la formula.

km=int(input("dar distancia en KM"))
h=int(input("dar tiempo en horas"))
v=km/h

print("la velociad es ",v,"km/h")
horas=6
hrs=10
kilometros=500
distancia=v/horas
distancia_dos=v/hrs
timepo=kilometros/v

print("Distancia recorrida en 6 hrs: ",distancia,"km")
print("Distancia recorrida en 10 hrs: ", distancia_dos,"km")
print("Tiempo para recorrer 500 km: ", timepo,"horas" )