#encoding: UTF-8

# Autor: Joaquin Rios Corvera A01375441
# Descripcion: Calcular cantidad de alumnos y repartición entre hombres y mujeres.

# A partir de aquí escribe tu programa

hombres = int(input("Cuántos hombres hay?"))
mujeres = int(input("Cuántas mujeres hay?"))

alumnos = hombres + mujeres

porcentajeHombres = hombres/alumnos*100
porcentajeMujeres = mujeres/alumnos*100

print("Total de inscritos:", alumnos)
print("Porcentaje de hombres:", round(porcentajeHombres,2))
print("Porcentaje de mujeres:", round(porcentajeMujeres,2))