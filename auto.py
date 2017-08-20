#encoding: UTF-8

# Autor: Omar Israel Galvan García A01745810
# Descripcion: Pregunta al usuario la velocidad a la que viaja un auto y calcula la
# distancia que recorrerá en 6 y 10 horas. Además el tiempo en el que recorerrá 500km

# velocidad = distancia/tiempo
# distancia = velocidad*tiempo
# tiempo = distancia/velocidad
velocidad = 0
distancia1 = 0
distancia2 = 0
tiempo = 0

velocidad = int(input("Velocidad del auto en km/h: "))  #pide al usuario la velocidad
distancia1 = (velocidad * 6)                            #se obtiene distancia 1
distancia2 = (velocidad * 10)                           #se obtiene distancia 2
tiempo = (500/velocidad)                                #se obtiene el tiempo

print("Distancia que recorre en 6 horas: ",distancia1, "km")   # se imprime la distancia 1
print("Distancia que recorre en 10 horas: ",distancia2,"km")  # se imprime la distancia 2
print("Tiempo en que recorrerá 500km: ", tiempo, "hrs.") # se imprime el tiempo







