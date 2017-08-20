#encoding: UTF-8

# Autor: Omar Israel Galván García A01745810
# Descripcion: Calcula el porcentaje de hombres y mujeres inscritos en una calse.

mujeres = int(input("Número de mujeres en la clase: "))
hombres = int(input("Número de hombres en la calse: "))
total = (hombres + mujeres)
totalhombres = ((hombres*100)/total)
totalmujeres = ((mujeres*100)/total)

print("Numero total de alumnos inscritos: ",total)
print("Porcentaje de mujeres: ",totalmujeres,"%")
print("Porcentaje de hombres: ",totalhombres,"%"    )





