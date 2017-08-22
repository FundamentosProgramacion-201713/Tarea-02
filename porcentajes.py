#encoding: UTF-8

# Autor: Neftalí Rodríguez Martínez, A01375808.
# Descripcion: Este programa lee el número de mujeres y hombres inscritos en una clase, calcula el número de alumnos
# inscritos, así como el porcentaje respectivo de mujeres y hombres.

# A partir de aquí escribe tu programa

num_mujeres = int (input("Ingrese el total de mujeres inscritas: "))
num_hombres = int (input("Ingrese el total de hombres inscritos: "))

totalalumnos = num_hombres + num_mujeres

porc_mujeres  = (num_mujeres * 100) / totalalumnos
porc_hombres = (num_hombres * 100) / totalalumnos

print("El número de alumnos inscritos es: ", totalalumnos)
print ("El porcentaje de mujeres inscritas es: ", porc_mujeres)
print ("El porcentaje de hombres inscritos es: ", porc_hombres)
