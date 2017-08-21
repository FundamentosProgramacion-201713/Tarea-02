#encoding: UTF-8

# Autor: Natalia Meraz Tostado, A01745008
# Descripcion: Crear un programa que muestre el porcentaje de mujeres y hombres inscritos en una clase

# A partir de aquí escribe tu programa

mujeres = input("Mujeres inscritas: ")
mujeres = int(mujeres)
hombres = input("Hombres inscritos: ")
hombres = int(hombres)

total = mujeres + hombres
porcentajemujeres = (mujeres * 100)/total
porcentajehombres = (hombres * 100)/total

print("Total de inscritos: ", total)
print("Porcentaje de mujeres: ",porcentajemujeres,"%")
print("Porcentaje de hombres: ",porcentajehombres,"%")
