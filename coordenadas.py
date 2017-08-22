import math
x=float(input("Ingrese la coordenada X"))
y=float(input("Ingrese la coordenada Y"))
hipotenusa=((x**2)+(y**2))**.5
angulo= (math.atan2(x,y))*(180/math.pi)
print("La magnitud de la hipotenusa es de",hipotenusa,"unidades")
print("El ángulo es de:",angulo,"grados")