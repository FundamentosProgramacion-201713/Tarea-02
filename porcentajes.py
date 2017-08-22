#encoding: UTF-8

# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# A partir de aquí escribe tu programa
mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))
total = mujeres + hombres

porcentajeMujeres = round((mujeres / total)* 100, 1)
porcentajeHombres = round((hombres / total)* 100, 1)

print("Total de inscritos: ", total)
print("Porcentaje de mujeres: ", porcentajeMujeres, "%", sep="")
print("Porcentaje de hombres: ", porcentajeHombres, "%", sep="")
