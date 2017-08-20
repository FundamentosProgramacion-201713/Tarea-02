#encoding: UTF-8

# Autor: José Antonio Gómez Mora, A01374459
# Descripcion: Calcula el porcentaje de hombres y mujeres inscritos en una clase.

# A partir de aquí escribe tu programa

mujeres=int(input("Escribe el total de mujeres en la clase: "))
hombres=int(input("Escribe el total de hombres en la clase: "))

total=mujeres+hombres

pMujeres=mujeres*100/total
pHombres=hombres*100/total

print("Mujeres inscritas:",mujeres)
print("Hombres inscritos:",hombres)
print("Total de alumnos:",total)
print("Porcentaje de mujeres",pMujeres)
print("Porcentaje de hombres",pHombres)

