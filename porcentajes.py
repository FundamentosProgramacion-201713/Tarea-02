#encoding: UTF-8

# Autor: Roberto Téllez Perezyera
# Este programa determina y muestra el total de alumnos inscritos en una clase, el porcentaje de hombres, y el
#porcentaje de mujeres; con base en los números de alumnos de cada género introducidos por el usuario.

# A partir de aquí escribe tu programa
strMujeres = (input("Teclee el número de mujeres inscritas en la clase: "))
strHombres = (input("Teclee el número de hombres inscritos en la clase: "))
mujeres = int(strMujeres)
hombres = int(strHombres)

totalClase = (mujeres + hombres)
percMujeres = (mujeres * 100) / totalClase
percHombres = (hombres * 100) / totalClase
#'perc' is short for 'percentage'

print ("-----")
print ("Hay ", totalClase, "alumnos inscritos en la clase.")
print ("El ", percMujeres, "% son mujeres.")
print ("El ", percHombres, "% son hombres.")