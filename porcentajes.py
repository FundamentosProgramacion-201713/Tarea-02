#encoding: UTF-8

# Autor: Alberto López Reyes, A01745811
# Descripcion: Este programa imprime el total de estudiantes y los porcentajes de sus sexos
# a partir de una cantidad de estudiantes hombres y mujeres otorgados.

# A partir de aquí escribe tu programa

intMujeres = int(input("Mujeres inscritas: "))
intHombres = int(input("Hombres inscritos: "))

intTotal = intHombres + intMujeres
fltPorcentaje_Hombres = (float(intHombres) * 100) / float(intTotal)
fltPorcentaje_Mujeres = (float(intMujeres) * 100) / float(intTotal)

print(str("Total de inscritos: " + str(intTotal)))
print(str("Porcentaje de mujeres: " + str(round(fltPorcentaje_Mujeres, 1)) + "%"))
print(str("Porcentaje de hombres: " + str(round(fltPorcentaje_Hombres, 1)) + "%"))
