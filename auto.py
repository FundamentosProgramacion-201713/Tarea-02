#encoding: UTF-8

# Autor: Jean Paul Esquivel Lobato, A01376152
# Descripcion: Encontrar distancia recorrida.

velocidad = float(input("¿A qué velocidad viaja el auto que ves? (km/h)"))
distancia6 = velocidad * 6
distancia10 = velocidad * 10
tiempo500 = 500 / velocidad

print("En 6hrs, se recorre", distancia6, "km")

print("En 10hrs, se recorre", distancia10, "km")

print("Para recorrer 500 km, se necesita ", round(tiempo500, 2), "hrs")
