#encoding: UTF-8

#Autor: Saúl Rodrigo Toral Luna, Matricula: A01745007
# Descripción: Calcular el costo de una comida en un restaurante, ademas de calcular el IVA y la propina

comida = input("ingresa el costo de su comida= ")

#calcular la propina de la comida
propina = float(comida) * (0.12)

#calcular el IVA de la comida
iva = float(comida) * (0.16)

#calcular el total
total = float(comida) + (propina) + (iva)

#imprimir los resultados
print("El costo de su comida es de: $",comida)
print("La propina es de: $", propina)
print("El iva es de: $", iva)
print("El total a pagar es de: $", total)

