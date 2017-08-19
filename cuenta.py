#encoding: UTF-8

# Autor: MARIA FERNANDA TORRES VELAZQUEZ, A01746537
# Descripcion: El siguiente programa calcula el iva, propina y total a pagar de una cuenta de comida introducida por el usuario.

# A partir de aquí escribe tu programa

subtotal= int(input("Por favor, introduzca el total de la comida: $  "))
iva= subtotal*.16
propina= subtotal*.12
total= subtotal+iva+propina
print("SUBTOTAL: $ ",subtotal)
print("IVA= ",iva)
print("PROPINA: ",propina)
print ("El total a pagar es: $",total)
