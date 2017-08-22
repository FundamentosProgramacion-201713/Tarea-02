#encoding: UTF-8

# Autor: Neftalí Rodríguez Martínez, A01375808.
# Descripcion: Este programa lee el costo de una comida sin propina ni iva,
# calcula el monto de las anteriores y entrega el costo total de la comida.

# A partir de aquí escribe tu programa

subtotalcomida = float (input("Ingrese el monto de la comida sin propina ni IVA: "))

propina = subtotalcomida * 0.12
iva = subtotalcomida * 0.16
costototal = subtotalcomida + propina + iva

print ("El subtotal de su comida es: ", subtotalcomida)
print ("El monto de propina es: ", propina)
print("El monto de IVA es: ", iva)
print("El total a pagar es: ", costototal)

