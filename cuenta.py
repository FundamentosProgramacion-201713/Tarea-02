#encoding: UTF-8

# Autor: Eduardo Gallegos Solís, A01745776
# Descripcion: Calcula la propina y el IVA de una cuenta.

# A partir de aquí escribe tu programa

cuenta = int(input("cuanto pagó por la comida?"))

subtotal= cuenta
propina = cuenta * 0.12
iva = cuenta * 0.16
total = (cuenta + propina + iva)

print("subtotal: $",subtotal)
print("propina: $",propina)
print("IVA: $",iva)
print("total: $",total)