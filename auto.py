#encoding: UTF-8

# Autor: Jordan González Bustamante, A01745993
# Descripcion: Programa que pide al usuario la velocidad que recorre un auto, y le arroja la distancia que recorre en
#              6, 10 horas, y lo que tardaría en recorrer 500 km

# -----
# distance = velocity * time

v = float(input("Ingresa la velocidad a la que viajas en números naturales (km/h): "))
d6 = str(v * 6)
d10 = str(v * 10)
t = str(500 / v)
if v > 500:
    message = " minutos"
else:
    message = " horas"
print("En 6 horas recorrerias: " + d6 + " km")
print("Y en 10 horas         : " + d10 + " km")
print("Para recorrer 500 km tardarias: " + t + message)


