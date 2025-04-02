#7. Crea un programa que pida al usuario una contraseña y siga pidiéndola hasta que cumpla con estos requisitos:
# Debe tener al menos 8 caracteres.
# Debe contener al menos un número.
# Debe contener al menos una letra mayúscula.

contraseña = input("Ingrese una contraseña: ")
while True:
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
    elif not any(char.isdigit() for char in contraseña):
        print("La contraseña debe contener al menos un número.")
    elif not any(char.isupper() for char in contraseña):
        print("La contraseña debe contener al menos una letra mayúscula.")
    else:
        print("Contraseña válida.")
        break
    
    contraseña = input("Ingrese una contraseña: ")