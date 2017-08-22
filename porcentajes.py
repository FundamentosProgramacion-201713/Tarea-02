#encoding: UTF-8

# Autor: Jose Heinz Moller Santos, A01375623
# Descripcion: Calcula el porcentaje de hombres y mujeres inscritos en una clase.

# A partir de aquí escribe tu programa

mujeres = int(input("Dame el número de mujeres: "))
hombres = int(input("Dame el número de hombres: "))

if (mujeres or hombres < 0):
    print("Dame un número verdadero")

else:

    totalAlumnos = mujeres + hombres
    print("Numero total de alumnos es: ",totalAlumnos)

    porcentajeHombres = (hombres*100)/totalAlumnos
    print("Porcentaje de hombres: ",porcentajeHombres)

    porcentajeMujeres = (mujeres*100)/totalAlumnos
    print("Porcentaje de mujeres: ",porcentajeMujeres)