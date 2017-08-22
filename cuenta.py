#encoding: UTF-8

# Autor: Alejandro VAlenzuela Guerrero, A01339478
# Descripcion: Sacar la propina, el IVA y total a pagar dependiendo el costo de una cuenta

# A partir de aquí escribe tu programa

costo = input ("Costo de comida:")
propina = float (costo) * .12
iva = float (costo) * .16
total = float (costo) + float (propina)+ float (iva)
print ("Propina:", propina)
print ("IVA:", iva)
print("Costo total comida:", total)