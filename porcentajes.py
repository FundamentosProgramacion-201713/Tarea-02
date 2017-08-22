#encoding: UTF-8

# Autor: Jordan González Bustamante, A01745993
# Descripcion: Programa que imprime porcentajes de alumnos, dividido en mujeres y hombres según lo ingresado por el
#              usuario.

# -----

m = float(input("Ingrese el total de hombres en números reales enteros: "))
w = float(input("Ingrese el total de mujeres en números reales enteros: "))
t = int(m + w)
mt = (m / t)*100
wt = (w / t)*100
t = str(t)
mt = str(mt)
wt = str(wt)
print("El numero total de alumnos es : " + t)
print("El porcentaje de hombres : " + mt + "%")
print("El porcentaje de mujeres : " + wt + "%")

