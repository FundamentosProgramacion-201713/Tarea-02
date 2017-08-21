#encoding: UTF-8

# Autor: Jose Antonio Vazquez Gabian
# Descripcion: programa que pregunte al usuario la velocidad a la que viaja un auto (km/h) y calcule lo siguiente

# A partir de aquí escribe tu programa

v=int(input("Velocidad del carro en (km/h): "))
t1=6
t2=10
d=500
d1=t1*v
d2=t2*v
t=d*v

print("Distancia en km recorrida por 6 hrs: ",d1)
print("Distancia en km recorrida por 10 hrs: ",d2)
print("Tiempo en horas necesaria para recorrer 500 km: ",t)

