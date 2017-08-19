#encoding: UTF-8

# Autor: Carlos Pano Hernandez, A01066264
# Descripcion: Calculadora del porcentaje de hombres y mujeres en un salón.

# A partir de aquí escribe tu programa

#Número de hombres y mujeres.
hombres = input("Hombres inscritos:")
hombres = int(hombres)

mujeres = input("Mujeres inscritas:")
mujeres = int(mujeres)

#Suma
totalSalon = hombres + mujeres
totalSalon = int(totalSalon)

#Porcentaje hombres
hombresPorcentaje = (hombres*100)/totalSalon

#Porcentaje mujeres
mujeresPorcentaje = (mujeres*100)/totalSalon

#Imprimir valores
print ("-----------------------------------------------")
print ("Total de inscritos:", totalSalon)
print ("-----------------------------------------------")
print ("Porcentaje de mujeres:", mujeresPorcentaje,"%")
print ("Porcentaje de hombres:", hombresPorcentaje,"%")
