#encoding: UTF-8

# Autor: Genaro Ortiz Durán, A01375315
# Calcular el total de alumnos inscritos en una clase, el porcentaje de hombres y el porcentaje de mujeres.


strA= input("Total de hombres inscritos en la clase:")
a= int(strA)

strB= input("Total de mujeres inscritas en la clase:")
b= int(strB)

Total=a+b
print("El total de alumnos es:", Total)

PorcentajeH=(a*100)/Total
print("El porcentaje de hombres inscritos es:", PorcentajeH,"%")

PorcentajeM=(b*100)/Total
print("El porcentaje de mujeres inscritos es:", PorcentajeM,"%")
