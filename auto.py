#encoding: UTF-8


# Autor: Alejandro Chávez Campos, A01374974
# Descripcion: Mi programa es sobre como determinar la distancia que recorre un auto en distintos tiempos, y en cuánto tiempo se tardaría en alcanzar una determinada distancia.


# A partir de aquí escribe tu programa

velocidadDelAuto=float(input("Dame la velocidad actual del auto en kilómetros/hora: "))
distancia6hrs=velocidadDelAuto*6
distancia10hrs=velocidadDelAuto*10
tiempo500km=500/velocidadDelAuto
print ("La velocidad del auto es:", velocidadDelAuto)
print ("La distancia que alcanzaría el auto después de 6 horas es:", distancia6hrs)
print ("La distancia que alcanzaría el auto después de 10 horas es:", distancia10hrs)
print ("Las horas que al auto le tomaría alcanzar los 500 kilómetros son:", tiempo500km)

