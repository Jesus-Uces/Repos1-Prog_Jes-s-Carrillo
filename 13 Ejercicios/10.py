# 10. Dada una lista de ventas con valores None cuando falta un dato, usa not en un ciclo para contar
#  cuántos valores faltan y calcular el promedio solo con los datos válidos.

lista_ventas = [100, 200, None, 300, None, 400, 500]
contador_faltantes = 0  
suma_ventas = 0
contador_validos = 0
print("Lista de ventas:", lista_ventas)
for venta in lista_ventas:
    if not venta:  # Si venta es None o 0, se cuenta como faltante
        contador_faltantes += 1
    else:
        suma_ventas += venta  # Sumar solo los valores válidos
        contador_validos += 1  

