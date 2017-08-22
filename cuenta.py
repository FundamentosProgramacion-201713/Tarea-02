#encoding: UTF-8

# Autor: Roberto Téllez Perezyera, A01374866
# Descripcion: Programa que calcula y muestra la propina, el IVA y el total a pagar por una comida a partir del costo
# introducido por el usuario.


# A partir de aquí escribe tu programa
strSubtotal = input("Por favor, introduzca el costo de su comida: ")
subtotal = float(strSubtotal)

propina = (subtotal * 0.12)
iva = (subtotal * 0.16)
totalAPagar = (subtotal + propina + iva)

print ("-----")
print ("Propina (12%): $", propina)
print ("IVA (16%): $", iva)
print ("Por pagar: $", totalAPagar)