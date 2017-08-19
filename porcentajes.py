#encoding: UTF-8

# Autor: MARIA FERNANDA TORRES VELAZQUEZ, A01746537
# Descripcion: El programa calcula el porcentaje de hombre y miujeres de una clase a partir de datos introducidos por elusuario.

# A partir de aquí escribe tu programa

mujeres= int(input("Introduce el numero de mujeres en la clase: "))
hombres= int (input("Introduce el numero de hombres en la clase: "))
total= hombres+mujeres
pm= (mujeres*100)/total
ph=(hombres*100)/total

print ("Total inscritos: ",total,"alumnos")
print ("Porcentaje mujeres: ",pm,"%")
print ("Porcentaje hombres: ",ph,"%")


