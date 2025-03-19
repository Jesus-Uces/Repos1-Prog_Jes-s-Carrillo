import random

# Paso 1: Generar pacientes aleatorios
pacientes = []
contador = 0
for i in range(10):
    paciente = {
        "ID":i+1,
        "FC":random.randint(50,130),
        "PA":random.randint(80,150)
    }
    pacientes.append(paciente)

# Paso 2: Función para clasificar pacientes
def clasificar_pacientes(frecuencia, presion):
    if 60<= frecuencia <= 100 and (presion in range(90,121)):
        return "Sano"
    elif frecuencia not in range(60,101) or presion not in range(90,121):
        return "En riesgo"
    else:
        return "Crítico"

# Paso 3: Clasificar datos generados
print("------Clasificación de pacientes aleatorios-------")
for paciente_clasificado in pacientes:
    estado = clasificar_pacientes(paciente_clasificado["FC"],paciente_clasificado["PA"])
    print(f'Paciente {paciente_clasificado["ID"]} ::: Estado {estado}')
# Paso 4: Permitir agregar más pacientes

# Datos de entrada INT
def entrada_int(mensaje, min, max):
    while True:
        try:
            valor = int(input(mensaje))
            if valor in range(min,max+1):
                return valor
            else:
                print(f"Los valores deben estar entre {min} y {max}")
        except ValueError as e:
            print("🙈 Valor debe dser de tipo entero ")

while True:
    continuar = input("Desea ingresar más pacientes? s/n: ").lower().replace(" ","").split()

    if continuar in ["n","no"]:
        print("💔Finalizó el programa")
        break
    else:
        fc = entrada_int("Ingresa la Frecuencia Cardiaca: ",50,130)
        pa = entrada_int("Ingresa la presión arterial: ",80,150)