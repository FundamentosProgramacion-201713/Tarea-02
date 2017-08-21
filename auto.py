
# Autor: Natalia Meraz Tostado, A01745008
# Descripcion: Desarrollar un programa el cual pregunte la velocidad e imprima distancia y tiempo

# A partir de aquí escribe tu programa

velocidad = input("Velocidad en km/h: ")
velocidad = float(velocidad)

distancia6 = 6 * velocidad
distancia10 = 10*velocidad
tiempo = 500/velocidad

print("Velocidad del auto en km/h: ", velocidad)
print("Distancia recorrida en 6 hrs: ", distancia6)
print("Distancia recorrida en 10 hrs: ", distancia10)
print("Tiempo para recorrer 500 km: ", tiempo)
