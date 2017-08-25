#encoding: UTF-8

# Autor: Dora Gabriela Lizarraga Gonzalez, A01229599
# Descripcion: Se calculara la distancia o tiempo que tarda un auto de acuerdo a la velocidad introducida.

# A partir de aquí escribe tu programa

velocidad = int(input('Velocidad del auto en km/h: '))
distancia6 = (velocidad*6)
distancia10 = (velocidad*10)
tiempo500 = (500/velocidad)
print (distancia6 , 'km')
print (distancia10 , 'km')
print (tiempo500 , 'hrs.')
