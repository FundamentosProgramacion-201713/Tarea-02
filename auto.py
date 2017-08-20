#encoding: UTF-8

# Autor: Luis Fernando Figueroa Rendon, A01746139
# Descripcion: Pedir la velocidad de un auto para sacar distancia y tiempo.

# A partir de aquí escribe tu programa

velocidad= input("Velocidad del auto en km/h: ")

velocidad= float(velocidad)

d=velocidad*6

d2=velocidad*10

t=500/velocidad

print("Distancia recorrida en 6 horas:", d)

print("Diastancia recorrida en 10 horas:", d2)

print("Tiempo para recorrer 500km:", t)