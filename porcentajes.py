#encoding: UTF-8

# Autor: Mónica Monserrat Palacios Rodríguez, A01375137
# Descripcion: Calcular el porcentaje de mujeres y hombres inscritos, calcular la cantidad total de inscritos.

# A partir de aquí escribe tu programa

m_i=int(input("Mujeres inscritas: "))
h_i=int(input("Hombres inscritos: "))

total=(m_i+h_i)
print("Total de inscritos:", total)

porc_m=(m_i*100)/total
print("Porcentaje de mujeres:", porc_m, "%")

porc_h=(h_i*100)/total
print("Porcentaje de hombres:", porc_h, "%")
