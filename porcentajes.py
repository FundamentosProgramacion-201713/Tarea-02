#encoding: UTF-8

# Autor:Rodrigo Rivera Salinas, A01375000
#  Descripcion: calcular el porcentaje de hombres y mujeres que estan en una clase

# A partir de aquí escribe tu programa

h=int(input("dar cantidad de hombres"))
m=int(input("dar cantidad de mujeres"))
total=h+m

hombres=(h*100)/total
mujeres=(m*100)/total

print("el porcentaje de hombres es: ",hombres, "%")
print("el porcentaje de mujeres es: ",mujeres, "%")

