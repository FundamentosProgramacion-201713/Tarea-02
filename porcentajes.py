#encoding: UTF-8

# Autor: Javier Pascal FLores A01375925
# Descripcion:Elabora un algoritmo y escribe un programa que calcula el porcentaje de hombres y mujeres inscritos en una clase.
#El programa le pregunta al usuario el número de mujeres y el número de hombres inscritos.
#Imprime:
#El número total de alumnos inscritos.
#El porcentaje de mujeres.
#El porcentaje de hombres.

# A partir de aquí escribe tu programa

hombres= input("¿Cuantos Hombres hay? ")
mujeres= input("¿Cuantas mujeres hay? ")
mujeres=int(mujeres)
hombres=int(hombres)
total=hombres+mujeres
porcentaje_mujeres=(mujeres*100)/total
porcentaje_hombres=(hombres*100)/total
print("El total de alumnos es: ", total, "personas")
print("El porcentaje de hombres es: ", porcentaje_hombres,"%" )
print("El porcentaje de mujeres es: ", porcentaje_mujeres,"%" )
