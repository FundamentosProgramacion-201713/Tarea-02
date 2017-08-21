#encoding: UTF-8

# Autor: Siham El Khoury Caviedes, A01374764
# Descripcion: Cálculo de alumnos inscritos.

# A partir de aquí escribe tu programa:
mujeres = int(input("Indique el número de mujeres inscritas: "))
hombres = int(input("Indique el número de hombres inscritos: "))
total = mujeres + hombres
porcentajeMujeres = (mujeres * 100) / total
porcentajeHombres = (hombres * 100) / total
print ("Total de inscritos:", total)
print ("Porcentaje de mujeres:", porcentajeMujeres)
print ("Porcentaje de hombres:", porcentajeHombres)
