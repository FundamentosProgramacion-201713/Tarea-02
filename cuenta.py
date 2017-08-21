#encoding: UTF-8

# Autor: Mónica Monserrat Palacios Rodríguez, A01375137
# Descripcion: Calcular la cuenta total

# A partir de aquí escribe tu programa
subtotal = int(input("Costo de tu comida: "))

propina=(subtotal*.12)
print("Propina: $", propina)

iva=(subtotal*.16)
print("IVA: $", iva)

costo_total=(subtotal + propina + iva)
print("Total a pagar: $", costo_total)


