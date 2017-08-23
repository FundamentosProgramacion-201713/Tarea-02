#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: a partir de los datos que nos dan de el numero de mujeres y hombres inscritos, se va a dar el total de personas incritas y el porcentaje de hombres y mujeres

mujeres = int(input("Numero de mujeres inscritas:"))
hombres = int(input("Numero de hombres inscritos"))

total = mujeres + hombres

porcentajeMujeres = (mujeres*100)/total)
porcentajeHombres = (hombres*100)/total)

print("Total de inscritos:", total)
print("Porcentaje de mujeres:", porcentajeMujeres, "%")
print("Porcentaje de hombres:", porcentajeHombres, "%")
