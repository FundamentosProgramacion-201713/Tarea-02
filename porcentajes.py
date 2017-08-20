#encoding: UTF-8

# Autor: Angel Ramírez Martínez, A01273759
# Descripcion: Determina el número de alumnos inscritos así como, el porcentaje de mujeres y el de hombres

# A partir de aquí escribe tu programa
nMujeres = int( input('¿Cuál es el número de mujeres inscritas? '))
nHombres = int( input('¿Cuál es el número de hombres inscritos? ' ))
totalA = nMujeres + nHombres
mujeresP = nMujeres*100/totalA
hombresP = nHombres*100/totalA
print('El número total de alumnos inscritos es de:', totalA, 'alumnos')
print('El porcentaje de mujeres inscritas es de:', mujeresP,'%')
print('El porcentaje de hombres inscritos es de:', hombresP,'%')
