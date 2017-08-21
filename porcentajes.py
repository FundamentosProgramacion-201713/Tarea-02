#encoding: UTF-8

# Autor: Jose Antonio Vazquez Gabian, A01746585
# Descripcion: programa que calcula el porcentaje de hombres y mujeres inscritos en una clase

# A partir de aquí escribe tu programa

hombres= int(input("Numero de hombres inscritos: "))
mujeres= int(input("Numero de mujeres inscritas: "))
total= hombres + mujeres
h=(hombres*100)/total
m=(mujeres*100)/total

print("Total inscritos: ",total)
print("Porcentaje de Hombres", h, "%")
print("Porcentaje de mujeres", m, "%")

