#encoding: UTF-8

# Autor: Jose Heinz Moller Santos, A01375623
# Descripcion: Calcula distancia en km cuando se le es dado una velocidad

# A partir de aquí escribe tu programa

velocidad = int(input("Dame el valor de la velocidad: "))

if (velocidad < 0):
    print("Dame un número verdadero")
else:

    tiempo1 = 6
    tiempo2 = 10

    distanciaA = velocidad*tiempo1
    print("Distancia recorrida en 6 Hrs: ",distanciaA),
    distanciaB = velocidad*tiempo2
    print("Distancia recorrida en 10 Hrs: ",distanciaB)
    tiempo500km = 500/velocidad
    print("Tiempo que tardas en recorrer 500 km: ",tiempo500km)
