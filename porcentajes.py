#encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez, A01375560
# Descripcion: Este programa calcula el porcentaje de mujeres y hombres inscritos en una clase

# A partir de aquí escribe tu programa
#1
mujeres = int(input("Cuantas mujeres estan inscritas en el grupo? "))
hombres = int(input("Cuantos hombres estan inscritos en el grupo? "))
#2
Total = mujeres + hombres
percMujeres = (mujeres * 100) / Total
percHombres = (hombres * 100) / Total
#3
print ("Total de inscritos:", Total)
print ("Porcentaje de mujeres:", str(percMujeres) + "%")
print ("Porcentaje de hombres:", str(percHombres) + "%")
