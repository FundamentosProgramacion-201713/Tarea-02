#encoding: UTF-8

# Autor: Sebastian Morales Martin, A01376228
# Descripcion: Este programa calcula el porcentaje de hombres y mujeres en un salón de clases

# Análisis
# Entrada: número de hombres y mujeres en el salón
# Salida: Número total de alumnos, porcentaje de hombres y mujeres
# Relación E/S: Fórmula para el porcentaje de niño/as en el salón, suma de ambos sexos para dar el total de alumnos

# A partir de aquí escribe tu programa

print("Porentajes.py")

print("")
print("------------------------------------------------------------")
print("")

h = input("Introduzca el número de Hombres en el salón: ")
hom = int(h)

print("")
print("------------------------------------------------------------")
print("")

m = input("Introduzca el número de Mujeres en el salón: ")
muj = int(m)

print("")
print("------------------------------------------------------------")
print("")

totalAlumnos = hom + muj

porHom = (hom*100)/totalAlumnos
porMuj = (muj*100)/totalAlumnos

print("1. Total de Alumnos:", totalAlumnos)

print("")

print("2. Porcentaje de Hombres:",  porHom, "%")

print("")

print("3. Porcentaje de Mujeres:",  porMuj, "%")

print("")
print("------------------------------------------------------------")   
