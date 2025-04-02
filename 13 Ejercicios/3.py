#3. Pide al usuario que ingrese calificaciones hasta que escriba "fin" 
# y calcula el promedio.

def promdio_calificaciones (cal_1,cal_2,cal_3):
    resultado = (cal_1 + cal_2 + cal_3)
    resultado = resultado / 3
    return resultado
cal_1 = float(input("Ingrese la calificación 1: "))
cal_2 = float(input("Ingrese la calificación 2: "))
cal_3 = float(input("Ingrese la calificación 3: "))
llamada = promdio_calificaciones(cal_1, cal_2, cal_3)
print("El promedio es: ", llamada)
print("Fin del programa")