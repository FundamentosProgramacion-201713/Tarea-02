#encoding: UTF-8

# Autor: Jean Paul Esquivel Lobato      A01376152
# Descripcion: Calcular cantidad de alumnos y repartición entre hombres y mujeres.


mujeres = int(input("Cuantas mujeres inscritas hay?: "))
hombres = int(input("Cuantos hombres inscritos hay?: "))

totalAlumnos = hombres + mujeres

porcentajeHombres = hombres * 100 / totalAlumnos
porcentajeMujeres = mujeres * 100 / totalAlumnos

print("Total de inscritos: ", totalAlumnos)
print("Porcentaje de mujeres: ", porcentajeMujeres, "%")
print("Porcentaje de hombres: ", porcentajeHombres, "%")