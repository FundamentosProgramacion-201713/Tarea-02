#encoding: UTF-8

# Autor: Juan Sebastián Lozano Derbez, A01374452
# Descripcion: Calcular distancias recorridas y tiempos necesarios para recorrer una distancia usando la velocidad.

# A partir de aquí escribe tu programa

velocidad = int(input("A qué velocidad va el auto?:"))

distancia1 = velocidad*6
distancia2 = velocidad*10
tiempo = 500/velocidad

print("Distancia en 6 horas:", distancia1, "km")
print("Distancia en 10 horas:", distancia2, "km")
print("Tiempo en el que se recorren 500km:", tiempo, "horas")
