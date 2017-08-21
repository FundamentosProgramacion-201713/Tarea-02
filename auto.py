#encoding: UTF-8

# Autor: Neftalí Rodríguez Martínez, A01375808.
# Descripción: En ese programa pregunto la velocidad de un auto al usuario y
# calculo y entrego la distancia recorrida en 6 y 10 horas, así como el tiempo que le llevará recorrer 500 kms.

# A partir de aquí escribe tu programa

print("Este programa pregunta al usuario la velocidad a la que viaja un auto"
      " e imprime distancia en 6 y 10 horas, así como el tiempo que le llevará "
      "recorrer 500 kms.")

velocidad = int (input("Escriba la velocidad de su auto: "))

distancia_6hrs = velocidad * 6
distancia_10hrs = velocidad * 10
tiempo_500kms = 500 / velocidad

print ("Su velocidad: ", velocidad)
print ("Distancia recorrida en 6 horas: ", distancia_6hrs)
print ("Distancia recorrida en 10 horas: ", distancia_10hrs)
print ("Tiempo que se tarda en recorrer 500 kms: ", tiempo_500kms)
