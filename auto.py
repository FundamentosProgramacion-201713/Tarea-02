#encoding: UTF-8

# Autor: Eduardo Gallegos Solís, A01745776
# Descripcion: Calcula el tiempo y la distancia que hace un automovil, a partir de la velocidad que se introduzca.

# A partir de aquí escribe tu programa
velocidad = int(input("Cuál es la velocidad del coche?"))

d6 = velocidad * 6
d10 = velocidad * 10
t = (500/ velocidad)

print(d6,"km")
print(d10,"km")
print(t,"hrs")