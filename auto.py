#encoding: UTF-8

# Autor: David Ramírez Ríos, A01338802
# Descripcion: Calcular tiempos de recurrido de un auto dada su velocidad.

# A partir de aquí escribe tu programa

velocidad = int (input("Tecela la velocidad."))
distanciaSeisHoras = velocidad * 6
distanciaDiezHoras = velocidad * 10
tiempo500Km = 500 / velocidad

print("Dsistancia recorrida en 6 hrs: ", distanciaSeisHoras, "km.")
print("Distancia recorrida en 10 hrs: ", distanciaDiezHoras, "km.")
print("Tiempo para recorrer 500 km: ", tiempo500Km, "horas.")
