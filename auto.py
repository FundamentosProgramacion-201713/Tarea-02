#----------------------------------------------------------------------------------------------------------------------
#encoding: UTF-8

# Autor: Sebastian Morales Martin, A01376228
# Descripcion: Resolver un problema matemático con la fórmula de velocidad

# A partir de aquí escribe tu programa

# Análisis
# Entrada: Constantes de distancia y tiempo+
# Salida: Aprximado de la velocidad en cada uno de los casos y el tiempo en el tercer caso
# relación E/S: Cálculo de la velocidad, tiempo, y distancia
#----------------------------------------------------------------------------------------------------------------------

print("Velocidad.py")
v = input ("Introduzca la Velocidad: ")
vel = float(v)
distanciaSeisHoras = vel * 6
distanciaDiezHoras = vel * 10
tiempoQuinientosKilometros = (500)/(vel)

print("------------------------------------------------") # líneas para estética
print("")

print("1. Distancia en 6 Horas:")
print("-", distanciaSeisHoras)

print("")

print("2. Distancia 10 Horas")
print("-", distanciaDiezHoras)

print("")

print("3. Tiempo para alcanzar los 500 km:")
print("-", tiempoQuinientosKilometros, "hora/s aprox.")

print("")

print("------------------------------------------------")



