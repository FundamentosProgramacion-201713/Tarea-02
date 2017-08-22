# Leonardo Castillejos Vite A01375332
# Un programa al cual le ingresas coordenadas cartesianas y te devuelve magnitud y ángulo
from math import sqrt
from math import atan2
from math import pi
x = int(input("Escriba la coordenada x " ))
y = int(input("Escriba la coordenada y "))
magnitud = sqrt(x**2 + y**2)
rad = atan2(y,x)
grad = rad * 180 / pi
print("La magnitud es:",magnitud)
print("El ángulo es:", grad)