##encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Realizar un programa que solicite al usuario introducir la distancia recorrida y el tiempo en el que un auto recorrio dicha distancia
# realizar la operacion para calcular la velocidad a partir de estos dos datos e imprimir en pantalla el resultado.

# A partir de aquí escribe tu programa

print ("                      Bienvenido - Calculo de la velocidad")
print ("")
velocidad = input("Introduce la velocidad del auto (en kilometros/hora):")
print("")
dato1 = int(velocidad) * 6
print("La distancia recorrida en 6 horas es de: ", dato1, "km")
dato2 = int(velocidad) * 10
print("La distancia recorrida en 10 horas es de: ", dato2, "km")
dato3 = 500 / int(velocidad)
print("El tiempo requerido para reccorrer 500 km es de: ", dato3, "horas")