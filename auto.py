#encoding: UTF-8

# Autor: José Antonio Gómez Mora, A01374459
# Descripcion: El usuario ingresa la velocidad en km/hr y el programa calcula la distancia en 6 y 10 hrs, tiempo en horas para recorrer 500 km.

# A partir de aquí escribe tu programa

velocidad=float(input("Escribir velocidad en Km/hr: "))
distancia6= velocidad*6
distancia10= velocidad*10
tiempo500=500/velocidad

print("Distancia recorrida en 6 horas:",int(distancia6),"km")
print("Distancia recorrida en 10 horas:",int(distancia10),"km")
print("Tiempo para recorrer 500 km: ",tiempo500,"horas")