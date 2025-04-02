#4. Crea una lista de temperaturas en grados Celsius y calcula el promedio, 
# la temperatura máxima y la mínima usando for.


# Lista de temperaturas en grados Celsius
temperaturas = [22, 25, 19, 30, 27, 21, 23]

# Inicialización de variables
suma_temperaturas = 0
temp_max = temperaturas[0]
temp_min = temperaturas[0]

# Cálculo de promedio, máxima y mínima
for temp in temperaturas:
    suma_temperaturas += temp
    if temp > temp_max:
        temp_max = temp
    if temp < temp_min:
        temp_min = temp

promedio = suma_temperaturas / len(temperaturas)

# Resultados
print(f"Promedio de temperaturas: {promedio:.2f}°C")
print(f"Temperatura máxima: {temp_max}°C")
print(f"Temperatura mínima: {temp_min}°C")