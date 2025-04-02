# 2. Escribe un programa que permita al usuario ingresar números y clasifique 
# cada uno como par o impar hasta que ingrese "0" para salir.

numero = int(input("Ingrese un número (0 para salir): "))
while numero != 0:
    if numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")
    numero = int(input("Ingrese un número (0 para salir): "))
    