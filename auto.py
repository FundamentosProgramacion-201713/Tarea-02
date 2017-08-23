#encoding: UTF-8

# Autor: Irving Fuentes Aguilera, A01745759
# Descripcion: Programa que calcula la distancia y tiempo que recorre una persona a derterminada velocidad o distancia.
# A partir de aquí escribe tu programa

velocidad= float(input("Insertar velocidad km/hr: "))

distancia6= 6 * velocidad
distancia10= 10 * velocidad
tiempo= 500/velocidad

print("La distancia en 6 hrs es: ", distancia6, "km")
print("La distancia en 10 hrs es: ", distancia10, "km")
print("El tiempo para recorrer 500 km es: ", tiempo, "hrs")



