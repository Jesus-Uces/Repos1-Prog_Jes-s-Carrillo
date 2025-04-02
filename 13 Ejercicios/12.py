# Lista de correos electrónicos
correos = ["usuario1@gmail.com", "usuario2hotmail.com", "usuario3@outlook", "usuario4@correo.com"]

# Contador de correos inválidos
correos_invalidos = 0

# Ciclo para verificar cada correo
for correo in correos:
    if not ("@" in correo and "." in correo):
        correos_invalidos += 1

print(f"Número de correos inválidos: {correos_invalidos}")