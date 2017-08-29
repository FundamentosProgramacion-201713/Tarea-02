
#encoding: UTF-8

# Autor: Javier León Alcántara , A01745532
# Descripcion: Calcula el porcentaje de hombres y mujeres inscritos en una clase.

mujeres = float(input("Escriba el total de mujeres inscritas"))
hombres = float(input("Escriba el total de hombres inscritos"))

total =  int(mujeres+hombres)
porcent_mujeres = ((mujeres*100)/total)
porcent_hombres = ((hombres*100)/total)

print("Total de inscritos:", total)
print("Porcentaje de mujeres:", porcent_mujeres, "%")
print("Porcentaje de hombres:", porcent_hombres, "%")
