#encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A01339478
# Descripcion: Total de hombres y mujeres inscritos y porcentaje de hombres y mujeres

# A partir de aquí escribe tu programa

nhombres = input("Numero de hombres inscritos:")
nmujeres = input("Numero de mujeres inscritas:")
total = int (nhombres) + int (nmujeres)
porcentajeh = (100 / total) * int (nhombres)
porcentajem = (100 / total) * int (nmujeres)
print("Total de inscritos:", total, "personas")
print("Porcentaje de hombres:", porcentajeh, "%")
print("Porcentaje de mujeres:", porcentajem, "%")

