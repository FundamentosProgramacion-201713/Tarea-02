#encoding: UTF-8

# Autor: Jaime Orlando López Ramos, A01374696
# Descripcion: Programa que pida al usuario la velocidad en km/h a la que viaja su automóvil e imprima la distancia
# que recorre el auto (después de 6 y 10 horas) y el tiempo necesario para que el auto recorra 500 km

# A partir de aquí escribe tu programa
v1 = input("Introduzca la velocidad de su auto en Km/h: ")
v = int(v1)
d_6= v*6
print("Su auto recorre", d_6, "Km, después de 6 horas")
d_10= v*10
print("Su auto recorre", d_10, "Km después de 10 horas")
t_500= 500/v
print("Su auto recorrerá 500 km en", t_500, "horas")