#encoding: UTF-8

# Autor: Pedro Cortés Soberanes A01374919
# Descripcion: Este programa calcula el porcentaje de hombres y mujeres y su total

nh = int(input ("Teclea el número de hombres inscritos: "))
nm = int(input ("Teclea el número de mujeres inscritas: "))

total = nh+nm

ph = (nh*100)/total
pm = (nm*100)/total

print ("Mujeres inscritas: ", nm)
print ("Hombres inscritos: ", nh)
print ("-Total de inscritos: ", total)
print ("-Porcentaje Mujeres: ", pm, "%")
print ("-Porcentaje Hombres", ph, "%")
