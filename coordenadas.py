#----------------------------------------------------------------------------------------------------------------------
#encoding: UTF-8

# Autor: Sebastian Morales Martin, A01376228
# Descripcion: cálculo de coordenadas cartesianas a coordenadas polares

# A partir de aquí escribe tu programa

# Análisis
#Entrada: coordenadas
# Salida: valor de la magnitud, valor del ángulo de la magnitud en grados
# Relación E/S: fórmula para la magnitud (teorema de pitágoras), magnitud (tangente ivertida) y grados (conversion de Radianes a Grados)
#----------------------------------------------------------------------------------------------------------------------
import math

print("-----------------------------------------------")
print("")

x = input("Introduzca el valor de X: ")
xNum = int(x)

y = input("Introduzca el valor de Y: ")
yNum = int(y)

print("")
print("-----------------------------------------------")
print("")

r = xNum**2 + yNum**2
rRaiz = math.sqrt(r)

rad = math.atan2(yNum,xNum)
grad = (rad) * (180/3.1416)

print("1. Valor de r:", rRaiz)
print("")
print("2. Grados totales:", grad)