#encoding: UTF-8

# Autor: Ana María López Soto, A01746134
# Descripción: Calcula total de alumnos y porcentaje de hombres y mujereS

# A partir de aquí escribe tu programa

totalMujeres = int(input("Ingrese cantidad de mujeres inscritas: "))
totalHombres = int(input("Ingrese cantidad de hombres inscritos: "))

totalInscritos = totalMujeres + totalHombres
porcentajeMujeres = round(totalMujeres * 100 / totalInscritos)
porcentajeHombres = round(totalHombres * 100 / totalInscritos)

print("Mujeres inscritas:", totalMujeres)
print("Hombres inscritos:", totalHombres)
print("Total inscritos: ", totalInscritos)
print("Porcentaje de mujeres: ", porcentajeMujeres, "%")
print("Porcentaje de hombres: ", porcentajeHombres, "%")
