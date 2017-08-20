#encoding: UTF-8

# Autor: Angel Ramírez Martínez, A01273759
# Descripcion: Determina la distancia que se ha recorrido en 6 y 10 horas a partir de la velocidad introducida por
# el usuario, además que determina el tiempo en el que se recorreran 500 km con la misma velocidad.

# A partir de aquí escribe tu programa

velocidad = int( input('Ingresa la velocidad a la que viaja un automovil en km/h '))
distancia_6 = velocidad*6
distancia_10 = velocidad*10
horas_500 = 500/velocidad
print('La distancia que se recorrerá en 6 horas a una velocidad de', velocidad, 'es:', distancia_6, 'kilometros')
print('La distancia que se recorrerá en 10 horas a una velocidad de', velocidad, 'es:', distancia_10, 'kilometros')
print('Las horas en las que se recorrerán 500 kilómetros a una velocidad de', velocidad, 'es:', horas_500, 'horas')

