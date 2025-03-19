# El siguiente código debe contar cuántas palabras tiene 
# cada oración en un diccionario y almacenar los resultados 
# en otro diccionario. Sin embargo, da un error. 
# Encuentra y corrige el problema.

oraciones = {
    "frase1": "Hola, ¿cómo estás?",
    "frase2": "Python es un lenguaje de programación.",
    "frase3": "Esto es una prueba."
}

conteo_palabras = {}
for clave, valor in oraciones.items():
    conteo_palabras[clave] = len(valor.split())

print(conteo_palabras) # Debería imprimir {'frase1': 3, 'frase2': 6, 'frase3': 4}