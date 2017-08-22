#encoding: UTF-8

# Autor: Sebastian Morales Martin, A01376228
# Descripcion: Ayuda al usuario a calcular su cuenta incluyendo el IVA y la propina a pagar

# Análisis
# Entrada: Subtotal de la cuenta
# Salida: Total de la cuenta con el IVA y la propina
# Relación E/S: el calculo del cubtotal para obtener el IVA y la propina

# A partir de aquí escribe tu programa

p = input ("Introduzca el subtotal de su comida: ")
subT = float(p)

iva = subT * 0.16

propina = subT * 0.12

print("--------------------------------------------------------------") #las líneas fueron agregadas para estética :3
print("")
print("1. Subtotal:", subT)
print("2. IVA:", iva)
print("3. Propina:", propina)
print("")
print("--------------------------------------------------------------")
print("")
totalAPagar = subT + iva + propina
print("Total a Pagar por la Cuenta:", totalAPagar)
