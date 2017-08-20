#encoding: UTF-8

# Autor: Luis Enrique Neri Pérez, A01745995
# Descripcion: PROGRAMA QUE DETERMINE EL TOTAL DE ALUMNOS Y EL PORCENTAJE DE HOMBRES Y MUJERES INSCRITOS A UNA CLASE.

print("ALUMNOS INSCRITOS")

hombresInscritos = int(input("Número de hombres inscritos: "))
mujeresInscritas = int(input("Número de mujeres inscritas: "))

totalInscritos = hombresInscritos + mujeresInscritas
porcentajeH = float(hombresInscritos/totalInscritos*100)
porcentajeM = float(mujeresInscritas/totalInscritos*100)

print("Hombres Inscritos:", hombresInscritos)
print("Mujeres Inscritas", mujeresInscritas)
print("Total de Alumos Inscritos", totalInscritos)
print("Porcentaje Hombres:", porcentajeH,"%")
print("Porcentaje Mujeres:", porcentajeM,"%")

