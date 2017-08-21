#Autor: José Antonio Gómez Mora

#Descripción: Convierte coordenadas cartesianas a coordenadas polares
import math

pi=3.1416

x=int(input("Ingresa el valor de 'X': "))
y=int(input("Ingresa el valor de 'Y': "))

magnitud= (x**2+y**2)**(1/2)
anguloPi= float(math.atan2(y,x))
anguloGrados= anguloPi*180/pi

print("Magnitud:",magnitud)
print("Ángulo",anguloGrados)




