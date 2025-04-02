# 1. Crea un programa que pida un número y cuente desde 1 hasta ese número,
# pero se detenga si el número ingresado no es positivo.

#solicita un numero al usuario
numero=int(input("Ingrese un número positivo: "))

#verifica si el numero es positivo
if numero>0:
#si es positivo cuenta desde 1 hasta el numero ingresado
    for i in range(1,numero+1):
        print(i)
else:
    #si no es positivo muestra un mensaje de error
    print("El número ingresado no es positivo.")

