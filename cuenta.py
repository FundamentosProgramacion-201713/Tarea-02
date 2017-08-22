#encoding: UTF-8

# Autor: Javier Pascal Flores, A01375925
# Descripcion:Elabora un algoritmo y escribe un programa que calcula el costo total de una comida en un restaurante.
#El programa le pregunta al usuario el total de la comida.
#Agrega 12% de propina y 16% de IVA.
#Cada porcentaje se calcula con respecto al costo de la comida.
#Imprime:
#El subtotal (costo de la comida)
#La propina.
#IVA.
#Total a pagar. (subtotal + propina + IVA)

# A partir de aquí escribe tu programa

subtotal=input("¿Cual fue el total de la comida? ")
subtotal = int(subtotal)
propina=0
iva=0
total_a_pagar=0
propina=subtotal*.12
iva=subtotal*.16
total_a_pagar=subtotal+propina+iva
print("El subtotal es: ", subtotal, "$")
print("El iva es: ", iva, "$")
print("la propina es: ", propina, "$")
print("El total a pagar es: ", total_a_pagar, "$")



