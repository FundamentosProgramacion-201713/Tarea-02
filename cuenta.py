#encoding: UTF-8

# Autor: Ernesto Ibhar Guevara Gomez, A01746121
# Descripcion: Imprime el total de la cuenta con Iva y propina.

# A partir de aquí escribe tu programa
comida=input("Costo de su comida: ")
comida=int(comida)

propina= comida * 0.12
iva= comida * 0.16
TotalAPagar= comida + propina + iva
print("Propina: ", propina)
print("IVA", iva)
print("Total a pagar: ", TotalAPagar)
