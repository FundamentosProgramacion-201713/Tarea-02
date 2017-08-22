#encoding: UTF-8

# Autor: Genaro Ortiz Durán, A01375315
# Descripcion: Crear algoritmo que pueda calcular la distancia recorrida en 6 y en 10 horas por un auto. Ver cuanto tiempo tarda el auto en recorrer 500km
tiempo=6
tiempo1=10

strA= input("Velocidad en km/h:")
a= int(strA)
Distancia= a*tiempo
Distancia1= a*tiempo1

Recorrer=(500/a)


print("La distancia en 6 horas es:",Distancia, "Km/h")
print("La distancia en 10 horas es:",Distancia1, "Km/h")
print("El tiempo que tarda en recorrer es:", Recorrer, "horas")





