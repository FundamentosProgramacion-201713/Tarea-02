#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: dando al programa la velocidad del auto en k/m este calcula la distancia que lleva recorrido un coche y el tiempo que le llevara para que llegue a 500km

str_velocidad = input("Velocidad del auto en km/h: ")
total_velocidad = int(str_velocidad)
#la formula de v=d/t la despejamos por lo que ahora es d=t*v y t=d/v
t1 = 6 #hrs
t2 = 10 #hrs
d1 = 500 #km
formula1 = (t1 * total_velocidad)
formula2 = (t2 * total_velocidad)
formula3 = (d1 / total_velocidad)
print("Distancia recorrida en 6 hrs:",formula1, "km")
print("Distancia recorrida en 10 hrs:",formula2, "km")
print("Tiempo para recorrer 500 km:", formula3, "hrs")
