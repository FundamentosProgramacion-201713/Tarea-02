#encoding: UTF-8

# Autor: Aaron Tonatiuh Villanueva Guzmán, A01375987
# Descripcion: Permite conocer la distancia que recorre un auto a una velocidad establecida en un periodo determinado así como el tiempo en el que recorre una distancia establecida.

# A partir de aquí escribe tu programa
velocidad=float(input("Ingrese la velocidad del auto en km/h"))
d6horas=velocidad*6
d10horas=velocidad*10
d500km=500/velocidad
print("la distancia recorrida en 6 horas es de:",d6horas,"km")
print("la distancia recorrida en 10 horas es de:",d10horas,"km")
print("se requieren:",d500km,"horas para que el auto recorra 500 km")

