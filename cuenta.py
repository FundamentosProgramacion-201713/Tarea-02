#encoding: UTF-8

# Autor: Aaron Tonatiuh Villanueva Guzmán, A01375987
# Descripcion: Calculador de cuentas en restaurantes. Permite añadir propina e iva del total e impreme las mismas así como el total a pagar

# A partir de aquí escribe tu programa
total=float(input("Ingrese el costo total de la comida del restaurante"))
propina=total*.12
iva=total*.16
print("propina: $",propina)
print("IVA: $",iva)
final=(total+propina+iva)
print("Total a pagar: $",final)