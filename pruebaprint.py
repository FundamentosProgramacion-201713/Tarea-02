# Autor: Andrea Montero Rivas
#Descripcion: Problema 5coordenadas

x=int(input("dame el valor de x",))
y=int(input("dame el valor de y",))

magnitud=(x**2 +y**2)**0.5
angulo=math.atan(y/x)

print(magnitud)
print(angulo)
