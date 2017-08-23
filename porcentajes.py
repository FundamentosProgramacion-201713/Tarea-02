#encoding: UTF-8

# Autor: Irving Fuentes Aguilera, A01745759
# Descripcion: Programa que calcula el total de la cuenta de una comida.
# A partir de aquí escribe tu programa

mujeres= int(input("Insertar # de mujeres: "))
hombres= int(input("Insertar # de hombres: "))
total= mujeres + hombres
porcentajemujeres= mujeres * 100 \
                   / total
porcentajehombres=  100- porcentajemujeres

print("total: ", total)
print("% de mujeres: ", porcentajemujeres)
print("% de hombres: ", porcentajehombres)


