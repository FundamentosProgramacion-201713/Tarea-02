# Autor: Eduardo Gallegos Solís, A01745776
# Descripcion: Calcula la magnitud y el ángulo de un vecto, dando sus componentes.

componentex = int(input("componente en x"))
componentey = int(input("componente en y"))

from math import atan2
from math import pi
magnitud = (componentex **2 + componentey **2) **.5
angulorad = atan2(componentey,componentex)

angulo = angulorad*180/pi
print(magnitud)
print(angulo)
