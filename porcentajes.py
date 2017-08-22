#encoding: UTF-8

# Autor: Ángel Guillermo Ortiz González, A01745998
# Descripcion: Cálculo del porcentaje de hombres y mujeres inscritos en una clase.

# A partir de aquí escribe tu programa

total_mujeres = int(input("Inserte el número de mujeres inscritos: "))
total_hombres = int(input("Inserte el número de hombres inscritos: "))
total_inscritos = total_mujeres + total_hombres

porcentaje_mujeres = total_mujeres * 100 / total_inscritos
porcentaje_hombres = 100 - porcentaje_mujeres

print ("Mujeres inscritas: ", total_mujeres, """
Hombres inscritos: """, total_hombres, """
Total de inscritos: """, total_inscritos, "alumnos", """
Porcentaje de mujeres: """, porcentaje_mujeres,"%", """
Porcentaje de hombres: """, porcentaje_hombres,"%")