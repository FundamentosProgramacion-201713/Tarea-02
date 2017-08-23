#encoding: UTF-8

# Autor: Daniel Ricardo Sahuer Balmaceda, A01375823
# Descripcion: Se pregunta por un subtotal y de acuerdo al monto escrito, se calcula la propina y el IVA, y se obtiene un total al sumar todas estas cantidades.

fltSubtotal = input("Costo de su comida: $ ")
subtotal = float(fltSubtotal)

propina = subtotal*.12
iva = subtotal*.16

total = subtotal + propina + iva

print ("Propina: $",propina,"\nIVA: $",iva,"\nTotal a pagar: $",total)