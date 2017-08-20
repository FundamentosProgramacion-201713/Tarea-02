#encoding: UTF-8

# Autor: Gabriela Mariel Vargas Franco, A01745775
# Descripcion: Calcular el porcentaje de hombres y mujeres inscritos en una clase.

# A partir de aquí escribe tu programa

strMujeres=input("Número de mujeres")
mujeres=int(strMujeres)
strHombres=input("Número de hombres")
hombres=int(strHombres)
#1.
totalAlumnos=mujeres+hombres
#2.
porcentajeMujeres=(mujeres/totalAlumnos)*100
#3.
porcentajeHombres=(hombres/totalAlumnos)*100

print("Total alumnos: ", totalAlumnos)
print("Porcentaje Mujeres: ", porcentajeMujeres)
print("Porcentaje Hombres: ", porcentajeHombres)
