#encoding: UTF-8

# Autor: Luis Daniel Rivera Salinas, A01374997
# Descripcion: Al ingresar cuantos hombres y cuantas mujeres hay en un salon, se imprimiran los porcentajes y el total

# A partir de aquí escribe tu programa

hombres = float(input("Ingrese el numero de hombres que hay: "))
mujeres = float(input("Ingrese el numero de mujeres que hay: "))

total = mujeres + hombres
porcentajeHombres = (hombres*100)/total
porcentajeMujeres = (mujeres*100)/total

print("El total es de : ", total, "alumnos")
print("El porcentaje de hombres es de: ", porcentajeHombres, "%")
print("El porcentaje de mujeres es de: ", porcentajeMujeres, "%")
