#encoding: UTF-8

# Autor: Alejandro Chávez Campos, A01374974
# Descripcion: Este programa es para obtener el IVA, la propina, ambas cantidades obtenidas sobre el costo de la comida, y mostrar el total.

# A partir de aquí escribe tu programa
costoComida=float(input("¿Cuál es el costo de la comida?: "))
propina=costoComida*0.12
iva= costoComida*0.16
total=propina+iva+costoComida
print("Costo de su comida: ",costoComida)
print("Propina: $",propina)
print("IVA: $",iva)
print("Total a pagar: $",total)
