#encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Este programa permite saber el porcentaje de hombres y mujeres, asi como el total de personas en una sala.

# A partir de aquí escribe tu programa

print("Bienvenidos")
print("")
print("El siguiente programa te permitira saber el porcentaje de hombres y mujeres inscritos en un salón")
print("")
hombres = input("Cantidad de hombres inscritos: ")
mujeres = input("Cantidad de mujeres inscritas: ")
total = int(hombres) + int(mujeres)
phombres = 100 / int(total) * int(hombres)
pmujeres = 100 / int(total) * int(mujeres)
print("")
print("El total de personas inscritas es: ", total)
print("Hay un ", phombres, "% de hombres")
print("Hay un ", pmujeres, "% de mujeres")