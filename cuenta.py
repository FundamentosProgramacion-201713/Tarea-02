#encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Este programa calcula los diferentes porcentajes extra a cobrar de una cuenta de comida.

# A partir de aquí escribe tu programa

print("Bienvenido")
print("")
print("El siguiente programa te permitira ccconocer información a cerca del pago que debes realizar")
print("por los alimentos que ingeriste el día de hoy")
totalComida = input("Costo de su comida: ")
propina = int(totalComida)*0.12
iva = int(totalComida)*0.16
total = int(totalComida) + int(propina) + int(iva)
print("")
print("Propina: ", propina)
print("IVA: ", iva)
print("Total a pagar: ", total)