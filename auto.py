#encoding: UTF-8

# Autor: Leonardo Castillejos Vite A01375332
# Descripcion: El usuario da una velocidad (Km/h) y el programa imprime cuantos kilometros recorrería en 6 y 10 horas y cuanto tardaría en recorrer 500 Km

# A partir de aquí escribe tu programa
velocidad = int(input("Escriba la velocidad del auto en Km/h "))

distancia1 = velocidad * 6
distancia2 = velocidad * 10
tiempo = 500/velocidad

print("La distancia recorrida en 6 horas es:", distancia1, "Km.")
print("La distancia recorrida en 10 horas es:", distancia2, "Km.")
print("El tiempo en recorrer 500 Km es:", tiempo, "horas.")
