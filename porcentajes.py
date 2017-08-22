#encoding: UTF-8

# Autor: Leonardo Castillejos Vite A01375332
# Descripcion: Un programa que a partir del número de hombres y mujeres da el total de alumnos y porcentaje de hombres y mujeres en la clase
# A partir de aquí escribe tu programa

mujeresins = int(input("Escriba el número de alumnas inscritas "))
hombresins = int(input("Escriba el número de alumnos inscritos "))
totalins = mujeresins + hombresins
porcenm = (mujeresins / totalins)*100
porcenh = (hombresins / totalins)*100
print("Total de alumnos", totalins)
print("Porcentaje de hombres ", porcenh, "%", sep="")
print("Porcentaje de mujeres ", porcenm, "%", sep="")