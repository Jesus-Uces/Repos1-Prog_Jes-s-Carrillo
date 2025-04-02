# 6. Crea un juego en el que el usuario debe adivinar un número secreto # (por ejemplo, 7). El programa debe seguir pidiendo intentos hasta 
# que el usuario acierte o ingrese "salir".

num_secreto = 7

print("Bienvenido al juego de adivinanza.")
print("Intenta adivinar el número secreto (entre 1 y 10).")
print("Escribe 'salir' para terminar el juego.")   

while True:
    intento = input("Ingresa tu intento: ")
    
    if intento.lower() == "salir":
        print("Gracias por jugar. ¡Hasta luego!")
        break
    
    try:
        intento = int(intento)
        
        if intento < 1 or intento > 10:
            print("Por favor, ingresa un número entre 1 y 10.")
            continue
        
        if intento == num_secreto:
            print("¡Felicidades! Adivinaste el número secreto.")
            break
        else:
            print("Intenta de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número o 'salir'.")
# Fin del programa
