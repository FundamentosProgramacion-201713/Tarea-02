#encoding: UTF-8

# Autor: Saul Rodrigo Toral Luna #Matricula: A01745007
# Descripción:  El programa calculará el total y el porcentaje de hombres y mujeres inscritos.

# Calcular:
#	El número total de alumnos inscritos.
#	El porcentaje de mujeres.
#	El porcentaje de hombres.


# 1.- El usuario ingresara valores para cantidad de mujeres y de hombres.

mujeres = input("Ingresa la cantidad de muejres inscritas: ")
hombres = input("Ingresa la cantidad de hombres inscritos: ")

#2.- Calcular el total de personas inscritas

total = (int(mujeres) + int(hombres))

#3.- Calcular los porcentajes para hombres y mujeres.

porcentajeHombres = (int(hombres) * (100)) / (int(total))
porcentajeMujeres = (int(mujeres) * (100)) / (int(total))

#4.- Imprimir resultados

print("El total de personas inscritas es de: ", total)
print("El porcentaje de mujeres es de: ", int(porcentajeMujeres),"%")
print("El porcentaje de Hombres es de: ", int(porcentajeHombres),"%")
