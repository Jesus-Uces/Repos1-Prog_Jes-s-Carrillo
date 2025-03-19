# El siguiente código debería verificar si una lista de 
# números está ordenada de menor a mayor, pero hay un 
# error lógico. Arréglalo.

def esta_ordenada(lista):
    print(len(lista))
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:  
            return False  
    return True  

numeros = [1, 2, 3, 4, 5]  
print(esta_ordenada(numeros))  # Debería imprimir True  