#

# Autor: Pablo García Morales, A01745530
# Descripcion: Queremos un programa para saber el porcentaje de mujeres y hombres de todos los estudiantes.

m=int(input("Numero de mujeres"))
h=int(input("Numero de hombres"))

Totalinscrito= m+h
mujeresporcentaje= (m*100)/Totalinscrito
hombresporcentaje= (h*100)/Totalinscrito
print(Totalinscrito)
print(mujeresporcentaje)
print(hombresporcentaje)
