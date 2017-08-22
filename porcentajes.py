#encoding: UTF-8

# Autor: Juan Sebastián Lozano Derbez, A01374452
# Descripcion: Calcular total de alumnos, numero de hombres y numero de mujeres

# A partir de aquí escribe tu programa

hom = (int(input("Hombres:")))
muj = (int(input("Mujeres:")))

total = muj + hom
porhom = hom * 100 / total
pormuj = 100 - porhom

print("Total:", total)
print("Porcentaje de hombres:", porhom )
print("Porcentaje de mujeres:", pormuj)