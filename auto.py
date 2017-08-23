#encoding: UTF-8

# Autor: Alberto López Reyes, A01745811
# Descripcion: Este programa calcula, basándose en la velocidad otorgada,
# la distancia del auto en 6 horas y 10 horas, y el tiempo en 500 km.

# A partir de aquí escribe tu programa

intVelocidad = int(input("Velocidad del auto en kh/h: "))

intTiempo_500km = 0
fltTiempo_500km = float(intTiempo_500km)

intDistancia_6hrs = intVelocidad * 6
intDistancia_10hrs = intVelocidad * 10
fltTiempo_500km = 500 / float(intVelocidad)

print(str("Distancia recorrida en 6hrs: " + str(intDistancia_6hrs) + " km"))
print(str("Distancia recorrida en 10hrs: " + str(intDistancia_10hrs) + " km"))
print(str("Tiempo para recorrer 500 km: " + str(fltTiempo_500km) + " hrs."))

