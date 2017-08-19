#encoding: UTF-8

# Autor: Carlos Pano Hernández, A01066264
# Descripcion: Agregar IVA y propina a la cuenta.

# A partir de aquí escribe tu programa

#Paso 1: Usuario agrega subototal
subtotal = input ("Agrega la cantidad a pagar sin IVA y propina:")
subtotal = int(subtotal)

#Paso 2: Calculo IVA
iva = (subtotal*116)/100

#Paso 3: Resta del subtotal al IVA
ivaFinal = (iva - subtotal)

#Paso 4: Calculo propina
propina = (subtotal*112)/100

#Paso 5: Resta del subtotal a la propina
propinaFinal = propina - subtotal

#Paso 6: Imprimi suma de subtotal, ivaFinal y propinaFinal
print ("")
print ("Propina:", "$", propinaFinal)
print ("IVA:", "$", ivaFinal)
print ("----------------------")
print ("Total a pagar:","$", subtotal + propinaFinal + ivaFinal)