#encoding: UTF-8

# Autor: Eduardo Gallegos Solís, A01745776
# Descripcion: ayuda a saber le porcentaje de hombres y de mujeres de una clase.

# A partir de aquí escribe tu programa
hombres = int(input("Cuántos hombres hay?"))
mujeres = int(input( "Cuántas mujeres hay?"))

alumnos = mujeres + hombres
porhombres = hombres / (alumnos/100)
pormujeres = mujeres / (alumnos/100)

print("El total de alumnos es",alumnos)
print("El porcentaje de hombres es",porhombres)
print("El porcentaje de mujeres es",pormujeres)
