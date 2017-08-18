#encoding: UTF-8

# Autor: Carlos Pano Hernandez, A01066264
# Descripcion: Se imprime la distancia recorrida en 6 y 10 hrs con cualquier velocidad en Km/h. Se imprime de igual manera el tiempo que toma recorrer 500 km.
# A partir de aquí escribe tu programa

#Paso 1: Introducir velocidad
velocidadValor= input ("Introduce la velocidad del coche:")
velocidad = int(velocidadValor)

#Paso 2: 6 hrs
distanciaSeis = velocidad*6

#Paso 3: 10 hrs
distanciaDiez = velocidad*10

#Paso 4: Tiempo para 500Km
tiempoQuinientos = 500/velocidad

#Paso 4: Imprimir 2, 3 y 4
print ("Distancia recorrida en 6 hrs:",distanciaSeis, "km")
print ("Distancia recorrida en 10 hrs:", distanciaDiez, "km")
print ("Tiempo para recorrer 500 km:", tiempoQuinientos, "hrs.")

