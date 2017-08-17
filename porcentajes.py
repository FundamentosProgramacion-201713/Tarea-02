#encoding: UTF-8

# Autor: Luis Miguel Baqueiro Vallejo, A01745997
# Descripcion: Problema 4

hombres = int(input("Cantidad de hombres: "))
mujeres = int(input("Cantidad de mujeres: "))
total = hombres + mujeres
porcentajeH = (hombres / total) * 100
porcentajeM = (mujeres / total) * 100
print("Mujeres inscritas: ", mujeres)
print("Hombres inscritos: ", hombres)
print("Total de inscritos: ", total)
print("Porcentaje de mujeres: ", porcentajeM, "%")
print("Porcentaje de hombres: ", porcentajeH, "%")
