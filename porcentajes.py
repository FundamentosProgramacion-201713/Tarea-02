#encoding: UTF-8

# Autor: Viviana Osorio Nieto, A01374461 
# Descripcion: Encontrar el porcentaje de hombres y mujeres. 

h = int(input("cuantos hombres hay?"))
m = int(input("cuantas mujeres hay?"))

t= h +m
ph = ( h*100)/t

pm = ( m*100)/t

print ("el total de alumnos es: ", t)
print ("el porcentaje de hombres es: ", ph)
print ("el porcentaje de mujeres es: ", pm) 

