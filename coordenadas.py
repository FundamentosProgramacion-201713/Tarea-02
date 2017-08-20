
# Autor: Omar Israel Galván García A01745810
#Descripción: Convierte coordenadas cartesianas a coordenadas polares.


import math    #Librería math: https://docs.python.org/2/library/math.html

x = int(input("Inserte el valor de x: "))             # Se obtiene el valor de x
y = int(input("Inserte el valor de y: "))             # Se obtiene el valor de y
angulo = math.degrees(math.atan2(y,x))                # Se obtiene el arcotangente de y/x y se tranforma a grados
r = ((x**2 + y**2)**0.5)                              # Se obtiene la magnitud
print("Magnitud:",r)                                  # Imprime los resultados
print("Angulo:",angulo)



