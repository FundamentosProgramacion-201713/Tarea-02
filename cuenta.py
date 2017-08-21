#encoding: UTF-8

# Autor: Siham El Khoury Caviedes, A01374764
# Descripcion: Cálculo de distancia y tiempo recorridos por un auto a cierta velocidad.

# A partir de aquí escribe tu programa:
v = int( input("Indique la velocidad (en números enteros) a la que viaja el auto:") )
t = 6
d = v * t
print ("La distancia recorrida en 6 horas es:", d)
t = 10
d = v * t
print ("La distancia recorrida en 10 horas es:", d)
d = 500
tiempo = d / v
print ("Tiempo en el que se recorren 500 kilómetros:", tiempo)