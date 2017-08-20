#encoding: UTF-8

# Autor: Ernesto Ibhar Guevara Gomez, A01746121
# Descripcion: Ingresas el numero de hombres y mujeres, el programa te da total de alumnos y porcentaje de hombre y mujeres.

# A partir de aquí escribe tu programa

hombres=input("Numero de hombres: ")
hombres=int(hombres)

mujeres=input("Numero de mujeres: ")
mujeres=int(mujeres)

Total= hombres + mujeres
porcentajem= ((mujeres * 100)/ Total)
porcentajeh= ((hombres *100) / Total)

print("Total: ", Total)
print("Porcentaje de mujeres: ", porcentajem)
print("Porcentaje de hombres: ", porcentajeh)

