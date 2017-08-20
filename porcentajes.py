#encoding: UTF-8

# Autor: Javier Martínez Hernández
# Descripcion: Se ingresaran el numero de alumnos, se sacara el total y el porcentaje de alumnos que son mujeres y hombres

mujeres=int(input("cuantas mujeres son: "))
hombres=int(input("cuantos hombres son: "))
total=mujeres+hombres
pormuj=(mujeres*100)/total
porhom=(hombres*100)/total

print("Total de alumnos: ", total, "\nPorcentaje de mujeres:", pormuj,"%", "\nPorcentaje de hombres:", porhom,"%")
