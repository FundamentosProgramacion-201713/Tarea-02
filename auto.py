#encoding: UTF-8

# Autor: Ivan Alejandro Dumas Martinez, A01375560
# Descripcion: Este programa muestra el recorrido de un carro despues de 6 y 10 horas, así como el tiempo que necesita para
# recorrer 500 km; de acuerdo a la velocidad introducida por el usuario.

# A partir de aquí escribe tu programa
#1
vel = int(input("A qué velocidad va el auto en km/h?"))

#2
hor6 = vel * 6
hor10 = vel * 10
dist500 = 500/vel

#3
print ("A las 6 horas el auto recorre:", str(hor6), "km")
print ("A las 10 horas el auto recorre:", str(hor10), "km")
print ("El auto recorre 500 km en:", str(dist500), "horas")
