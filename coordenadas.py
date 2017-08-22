# Autor: David Ramrírez Ríos, A01338802

# Descripción: Convertir coordenadas cartesianas a polares.


x = int (input("Teclea el valor x: "))
y = int (input("Teclea el valor y: "))

# angulo = atan2(x,y) No lo reconoce, ninguna función trigonométrica.


magnitud = ((x**2) + (y**2))**.5

print("Magnitud = ", magnitud)