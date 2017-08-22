#encoding: UTF-8

# Autor: Ángel Guillermo Ortiz González, A01745998
# Descripción: Conversión de coordenadas cartesianas a coordenadas polares.

valor_x = float(input('Inserte el valor de "x": '))
valor_y = float(input('Inserte el valor de "y": '))

magnitud = ( (valor_x ** 2) + (valor_y ** 2) ) ** 0.5
angulo = atan2(y/x)

print ("x: ", valor_x, """
y: """, valor_y, """
Magnitud""", magnitud, """
Angulo""", angulo)