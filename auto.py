#encoding: UTF-8

# Autor: Joaquin Rios Corvera A01375441
# Descripcion: Encontrar distancia recorrida en tiempo y tiempo
#necesario para viajar distancia.
# A partir de aquí escribe tu programa

velocidad = float(input("A qué velocidad viaja el auto? (km/h)"))
distancia6 = velocidad * 6
distancia10 = velocidad * 10
tiempo500 = 500/velocidad

print("En 6hrs, se recorren", distancia6, "km")
print("En 10hrs, se recorren", distancia10, "km")
print("Para recorrer 500km, se necesitan", round(tiempo500,2), "hrs")