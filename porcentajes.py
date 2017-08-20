#encoding: UTF-8

# Autor: Jaime Orlando López Ramos, A01374696
# Descripcion: Un programa que pregunte al usuario por el número de hombres y mujeres inscritos en un programa
# Y el porcentaje que hay de cada género

# A partir de aquí escribe tu programa
m= input("Ingrese el número de mujeres inscritas en el programa: ")
m= int(m)
h= input("Ingrese la cantidad de hombres inscritos en el programa: ")
h= int(h)
t= h+m
pm= m*100/t
ph= h*100/t
print("El total de alumos inscritos fue de:", t)
print("De los cuales, el", pm, "% eran mujeres")
print("Y el", ph, "% eran hombres")