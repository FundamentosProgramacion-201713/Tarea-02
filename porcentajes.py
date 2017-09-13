# encoding: UTF-8

# Autor: Andrea Montero Rivas, A01374496
# Descripcion: problema 4, porcentaje alumnos

mujeres = (int(input("Cuantas mujeres hay inscritas", )))
hombres = (int(input("Cuantos hombres hay inscritos", )))
total = mujeres + hombres
print(total)
p_mujeres = (mujeres * 100) / total
p_hombres = (hombres * 100) / total
print(p_mujeres)
print(p_hombres)