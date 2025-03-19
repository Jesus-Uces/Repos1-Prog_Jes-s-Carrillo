# Paso 1: Generar pacientes aleatorio

import random   # Importar librería random
# Crear lista vacía pacientes   
pacientes = []
# Inicializar contador  
contador = 0
# Iterar 10 veces
for i in range(10):
    # Crear diccionario paciente
    paciente = {
        "ID":i+1,
        "FC":random.randint(50,130),
        "PA":random.randint(80,150)
    }
    pacientes.append(paciente)
    