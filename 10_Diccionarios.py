# Diccionarios

# Crear el primer diccionario 'teclado1' con detalles de un teclado
teclado1 = {
    'Categoría': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
}

# Crear el segundo diccionario 'teclado2' con detalles de otro teclado
teclado2 = {
    'Categoría': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
}

# Imprimir el modelo y precio del teclado2
print('El modelo', teclado2['Modelo'], 'cuesta', teclado2['Precio'], '$.')

# Iterar sobre el diccionario teclado1 e imprimir cada clave y valor
for x, y in teclado1.items():
    # 'x' es la clave, 'y' es el valor
    # Se imprime cada par clave-valor en formato "clave: valor."
    print(x, ": ", y, ".")

# Eliminar el diccionario teclado1
del teclado1

# Eliminar las claves 'Categoría' y 'Precio' del diccionario teclado2
del teclado2["Categoría"]
del teclado2["Precio"]

# Imprimir el diccionario teclado2 después de eliminar las claves
# Solo queda la clave 'Modelo'
print(teclado2)

# Iterar sobre el diccionario teclado2 e imprimir la última clave que queda
for x, y in teclado2.items():
    # 'x' es la clave, 'y' es el valor
    # Se imprime el par clave-valor en formato "clave: valor."
    print(x, ": ", y)
