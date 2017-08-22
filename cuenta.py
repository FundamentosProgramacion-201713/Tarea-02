#encoding: UTF-8

# Autor: Jose Heinz Moller Santos, A01375623
# Descripcion: Saca el subtotal, la propina, el IVA y el total del costo de una comida

# A partir de aquí escribe tu programa

costo = int(input("Cuánto fue de la comida: "))

if (costo < 0):
    print("Dame un número verdadero")

else:

    propina = costo*0.12
    iva = costo*0.16

    total = costo+propina+iva

    print("Propina: ",propina)
    print("Porcentaje IVA:",iva)
    print("Total de los gatos: ",total)