#encoding: UTF-8

# Autor: Luis Fernando Figueroa Rendon, A01746139
# Descripcion: Sacar el total y porcentaje de hombres y mujeres inscritos.

# A partir de aquí escribe tu programa

hombres= input("Hombres inscritos: ")

mujeres= input("Mujeres inscritas: ")

hombres=float(hombres)

mujeres=float(mujeres)

total= hombres + mujeres

total=float(total)

porcentajeH = (hombres*100) / total

porcentajeM = (mujeres*100) / total

print("Total del inscritos:", total)

print("Porcentaje de hombres:", porcentajeH, "%")

print("Porcentaje de mujeres:", porcentajeM, "%")