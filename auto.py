#encoding: UTF-8

# Autor: Javier Martínez Hernández A01375496
# Descripcion: Sacar distancia y tiempo de un auto, se le pregunta al usuario la velocidad del auto

velocidad=int(input("velocidad del auto en km/h: "))
distancia6=velocidad*6
distancia10=velocidad*10
tiempo500=500/velocidad

print("Distancia recorrida en 6 horas: ", distancia6,"\nDistancia recorrida en 10 horas: ", distancia10)
print("Tiempo para recorrer 500km: ",tiempo500)
