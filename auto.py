#encoding: UTF-8

# Autor: Luis Daniel Rivera Salinas, A01374997
# Descripcion: Es un programa que al ingresar la velocidad a la que se va en un auto (en kilometros / hora) imprime la distancia recorrida en 10 y 6 horas y el tiempo en que tarda en recorrer 500 km

# A partir de aquí escribe tu programa

velocidad = int(input("Ingrese la velocidad del auto en Km/h: "))

velocidad6h = velocidad*6
velocidad10h = velocidad*10
tiempo500km = float(500/velocidad)

print("La velocidad del auto es: ", velocidad)
print("La distancia recorrida en 6 horas es de : ", velocidad6h, "metros")
print("La distancia recorrida en 10 horas es de : ", velocidad10h, "metros")
print("El tiempo que se tarda en recorrer 500 km es de : ", tiempo500km, "horas")