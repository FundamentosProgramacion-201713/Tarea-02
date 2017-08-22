#encoding: UTF-8

# Autor: Raul Ortiz Mateos A01375407
# Descripcion: mediante la cuenta calcular el IVA y la propina

# A partir de aquí escribe tu programa

TotalDelaComida= 7896
propina=  TotalDelaComida * .12
Iva= TotalDelaComida * .16
totalAPagar= TotalDelaComida + propina + Iva
print("el costo de la comida es de:", TotalDelaComida)
print("la propina es:", propina)
print("el Iva es de:", Iva)
print("el total a pagar", totalAPagar)


