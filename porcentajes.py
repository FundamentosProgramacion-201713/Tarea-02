#encoding: UTF-8

# Autor: Nazdira Abigail Cerda del Prado, A01375428
# Descripcion: A base del número de mujeres y de hombres inscritos calcula el total de alumnos, el porcentaje de mujeres y el porcentaje de hombres.

# A partir de aquí escribe tu programa

mujeresc=int(input("Número de mujeres:"))
hombresc=int(input("Número de hombres:"))

totalalumnos=mujeresc+hombresc
porcentajemujeres=(mujeresc*100)/totalalumnos
porcentajehombres=(hombresc*100)/totalalumnos

print("Total de alumnos:")
print(totalalumnos)
print("Porcentaje de mujeres:")
print(porcentajemujeres)
print("Porcentaje de hombres:")
print(porcentajehombres)