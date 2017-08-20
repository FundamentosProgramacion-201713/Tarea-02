#encoding: UTF-8

# Autor: Ernesto Ibhar Guevara Gomez, A01746121
# Descripcion: Imprime la distancia recorrida en 6 horas y 10 horas ingresando la velocidad. Tambien imprime el tiempo que tarda en recorrer 500 km un auto.

# A partir de aquí escribe tu programa

#Solicitar velocidad
ValorDeVelocidad=input("Introduce la velocidad: ")
velocidad=int(ValorDeVelocidad)
#Calcuar d1, d2, H
d1= velocidad * 6
d2= velocidad * 10
H= 500 / velocidad
#Imprimir resultados
print(d1, "km")
print(d2, "km")
print(H, "hrs")


