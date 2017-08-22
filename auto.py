#encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A0133478
# Descripcion: Saber cuenta distancia recorre un auto y en cuanto tiempo lo hace dependiendo de su velocidad

# A partir de aquí escribe tu programa =

velocidad = input ("Velocidad en km/h:")
distancia1 = int (velocidad) * 6
distancia2 = int (velocidad) * 10
tiempo = 500 / int (velocidad)
print ("Distacia recorrida en 6 hrs:", distancia1, "kilometros")
print ("Distacia recorrida en 10 hrs:", distancia2, "kilometros")
print ("Tiempo para recorrer 500 km/h:", tiempo, "horas")
