# 9. Genera una lista de 100 números aleatorios entre 1 y 100 y calcula el número más frecuente.

lista = []
frecuencia = {} 
import random
for i in range(100):
    lista.append(random.randint(1,100)) 
for num in lista:
    if num in frecuencia:
        frecuencia[num] += 1
    else:
        frecuencia[num] = 1
max_frecuencia = max(frecuencia.values())
numeros_frecuentes = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
print("Lista de números aleatorios:", lista)
print("Número(s) más frecuente(s):", numeros_frecuentes)
print("Frecuencia:", max_frecuencia)
print("Fin del programa")
