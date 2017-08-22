#encoding: UTF-8

# Autor:Rodrigo Rivera Salinas, A01375000
# Descripcion: a partir de la cuenta de comida sacar iva, propina y total
# A partir de aquí escribe tu programa

comida=int(input("dar cuanto costo la comida sin propina"))
prop=.12
iva=.16
propina=comida*prop
impu=comida*iva

total=comida+propina+impu

print("comida: ",comida)
print("propina", propina)
print("iva", impu)
print("la comida con impuesto y propina es de:", total)

