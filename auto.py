#encoding: UTF-8

# Autor: Ángel Guillermo Ortiz González, A01745998
# Descripcion: Cálculos respecto a la velocidad de un auto, la distancia que recorre y el tiempo en el que lo hace.

# A partir de aquí escribe tu programa

velocidad = float(input("Inserta la velocidad a la que viaja el auto en km/h: "))
distancia_6_hrs = 6 * velocidad
distancia_10_hrs = 10 * velocidad
tiempo_500_km = 500 / velocidad

print("Velocidad del auto en km/h: ", velocidad, """
Distancia recorrida en 6 hrs: """, distancia_6_hrs,"km", """
Distancia recorrida en 10 hrs: """, distancia_10_hrs, "km", """"
Tiempo para recorrer 500 km: """, tiempo_500_km, "hrs")

