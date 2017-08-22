#encoding: UTF-8

# Autor: David Ramírez Ríos, A01338802
# Descripcion: Calcular porcentaje de hombres y mujeres.

# A partir de aquí escribe tu programa

hombres = int (input("Teclea el número de hombres: "))
mujeres = int (input("Teclea el número de mujeres: "))
totalAlumnos = hombres + mujeres
porcentajeHombres = hombres * 100 / totalAlumnos
porcentajeMujeres = mujeres * 100 / totalAlumnos

print("Total de inscritos: ", totalAlumnos)
print("Porcentaje de mujeres: ", porcentajeMujeres, "%")
print("Porcentaje de hombres: ", porcentajeHombres, "%")