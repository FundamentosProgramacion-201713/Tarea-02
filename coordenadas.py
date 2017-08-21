#encoding: UTF-8

# Autor: Siham El Khoury Caviedes, A01374764
# Descripcion: Conversión de coordenadas cartesianas a polares.

x = int(input("Indique el valor de x en números enteros: "))
y = int(input("Indique el valor de y en números enteros: "))
magnitudr = ((x**2 + y**2)) ** 0.5
angulo = atan2(y,x)
print ("La magnitud es:", magnitudr)
print ("El ángulo es:", angulo)