#encoding: UTF-8

# Autor: Dora Gabriela Lizarraga Gonzalez, A01229599
# Descripcion: Este programa calculara la densidad de genero en los estudiantes.

# A partir de aquí escribe tu programa


mujeres = int(input('Cantidad de mujeres inscritas: '))
hombres = int(input('Cantidad de hombres inscritos: '))
totalAlumnos = (mujeres + hombres)
porcentajeM = (mujeres / totalAlumnos)*100
porcentajeH = (hombres / totalAlumnos)*100
print('Alumnos inscritos: ' , totalAlumnos)
print('Porcentaje de mujeres: ' , porcentajeM,'%')
print('Porcentaje de hombres: ' , porcentajeH,'%')
