# Autor: Eduardo Gallegos Solís, A01745776
# Descripcion: Calcula la magnitud y el ángulo de un vecto, dando sus componentes.

componentex = int(input("componente en x"))
componentey = int(input("componente en y"))

magnitud = (componentex **2 + componentey **2) **.5
angulo = atan2(componentey,componentex)

print(magnitud)
print(angulo)
