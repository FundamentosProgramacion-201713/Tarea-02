#encoding: UTF-8

# Autor: Aaron Tonatiuh Villanueva Guzmán, A01375987
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# A partir de aquí escribe tu programa
hombres=int(input("Número de hombres inscritos"))
mujeres=int(input("Número de mujeres inscritas"))
total=hombres+mujeres
porcentajehombres=(hombres/total)*100
porcentajemujeres=(mujeres/total)*100
print("el total de alumnos es:",total)
print("El porcentaje de hombres inscritos es",porcentajehombres,"%")
print("El porcentaje de mujeres inscritas es",porcentajemujeres,"%")

