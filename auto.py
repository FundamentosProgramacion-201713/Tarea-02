#encoding: UTF-8

# Autor: Gabriela Mariel Vargas Franco, A01745775
# Descripcion: Preguntar al usario la velocidad a la que viaja un auto (km/h) y que imprima: la distancia en km que recorre en 6 hrs, la distancia en km que recorre en 10hrs y el tienpo que requiere para recorrer 500 km.


# A partir de aquí escribe tu programa
strVelocidad= input("¿Velocidad?")
Velocidad=int(strVelocidad)
#1.
tiempo=6
distancia= Velocidad*tiempo
print("Distancia recorrida en 6hrs:", distancia, "km")
#2.
tiempo=10
distancia= Velocidad*tiempo
print("Distancia recorrida en 10hrs:", distancia, "km")
#3.
distancia=500
tiempo=distancia/Velocidad
print("Tiempo para recorrer 500 km:", tiempo, "hrs")



