#encoding: UTF-8

# Autor: Luis Daniel Rivera Salinas, A01374997
# Descripcion: Al ingresar lo que se paga de subtotal en un restaurante, se calcula la propina y el iva y se agrega para crear el total

# A partir de aquí escribe tu programa

costo = float(input("Ingrese el costo de su comida: "))

propina = float(costo*.12)
IVA = float(costo*.16)
total = float(costo + propina + IVA)

print("El subtotal es de: ", costo, "$")
print("La propina es de: ", propina, "$")
print("El IVA es de: ", IVA, "$")
print("El total a pagar es de: ", total , "$")