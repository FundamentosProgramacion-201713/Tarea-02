#encoding: UTF-8

# Autor: Javier León Alcántara , A01745532
# Descripcion: Calcula distancia y tiempo

velocidad = float(input("Escriba la velocidad en km/h"))

distancia_6 = (velocidad*6)
distancia_10 = (velocidad*10)
tiempo_500 = (500/velocidad)

print("La distancia en km. que recorre en 6 horas es : ",distancia_6, "km.")
print("La distancia en km. que recorre en 10 horas es : ",distancia_10, "km.")
print ("El tiempo en horas que requiere para recorrer 500 km. es : ",tiempo_500, "horas")

