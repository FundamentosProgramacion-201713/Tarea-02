#encoding: UTF-8

# Autor: Daniel Ricardo Sahuer Balmaceda, A01375823
# Descripcion: Se pregunta por el total de hombres y de mujeres inscritos, y se calcula el porcentaje para hombres y mujeres

fltMujeres = input("Mujeres inscritas: ")
mujeres = int(fltMujeres)

fltHombres = input("Hombres inscritos: ")
hombres = int(fltHombres)

total = mujeres + hombres
x = total/100

porcentajeHombres = hombres/x
porcentajeMujeres = mujeres/x

print ("Total de inscritos: ",total,"\nPorcentaje de mujeres: ",porcentajeMujeres,"%\nPorcentaje de hombres: ",porcentajeHombres,"%")