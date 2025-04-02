# 11. Pide al usuario que ingrese edades separadas por espacios y usa or en un ciclo para clasificar 
# cuántas personas son menores de edad (< 18), adultos (18-59) y adultos mayores (>= 60).

#
# Función para clasificar edades
def clasificar_edades(edades):
    menores = 0
    adultos = 0
    adultos_mayores = 0

    for edad in edades:
        if edad < 18:
            menores += 1
        elif edad >= 18 and edad < 60:
            adultos += 1
        else:
            adultos_mayores += 1

    return menores, adultos, adultos_mayores   


# Solicitar al usuario que ingrese edades separadas por espacios
edades_input = input("Ingrese edades separadas por espacios: ")
edades = list(map(int, edades_input.split()))  # Convertir a lista de enteros

