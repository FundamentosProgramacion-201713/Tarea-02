#encoding: UTF-8

# Autor: Alejandro Chávez Campos, A01374974
# Descripcion: Este programa es para obtener el porcentaje de hombres y mujeres.

# A partir de aquí escribe tu programa
mujeres = int(input("¿Cuántas mujeres hay?: "))
hombres = int(input("¿Cuántos hombres hay?: "))
total = hombres + mujeres
porcentajeMujeres = (mujeres * 100) / total
porcentajeHombres = (hombres * 100) / total
print("Mujeres inscritas: ", mujeres)
print("Hombres inscritos: ", hombres)
print("Total de inscritos: ", total)
print("Porcentaje de mujeres: ", porcentajeMujeres, "%")
print("Porcentaje de hombres: ", porcentajeHombres, "%")

