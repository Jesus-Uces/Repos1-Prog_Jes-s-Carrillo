import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("Escribe 'salir' para terminar el juego.")

    while True:
        usuario = input("Elige piedra, papel o tijera: ").lower()
        if usuario == "salir":
            print("¡Gracias por jugar! Hasta luego.")
            break
        if usuario not in opciones:
            print("Opción no válida. Intenta de nuevo.")
            continue

        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")

        if usuario == computadora:
            print("¡Es un empate!")
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("Perdiste. ¡Suerte la próxima vez!")

if __name__ == "__main__":
    jugar()