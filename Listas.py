# LISTAS
paises = ['México', 'Estados Unidos', 'Canadá', 'Argentina', 'Brasil']  # Se crea una lista de países
print('Lista de paises', paises)  # Se imprime la lista completa de países

# Imprimir cada país por separado accediendo a cada índice
print('Lista país por país:', paises[0], paises[1], paises[2], paises[3], paises[4])

# Imprimir la lista empezando por el final usando índices negativos
print('Lista empezando por el final:', paises[-1], paises[-2], paises[-3], paises[-4], paises[-5])

# Eliminar un país de la lista por índice (el país en la posición 4, que es 'Brasil')
del paises[4]
print('Lista con un País eliminado:', paises)

# Eliminar otro país de la lista, esta vez por su valor ('Estados Unidos')
paises.remove('Estados Unidos')
print('Lista con otro País eliminado:', paises)

# Eliminar y guardar el primer país de la lista (posición 0) usando pop()
guardado = paises.pop(0)
print('Lista con pais cortado:', paises)  # Se imprime la lista sin el país eliminado

# Imprimir el país que fue eliminado y guardado
print('País guardado:', guardado)

# Agregar un nuevo país al final de la lista usando append()
paises.append('Colombia')
print('Lista con nuevo País agregado al final:', paises)

# Insertar países en posiciones específicas usando insert()
paises.insert(0, 'Ecuador')  # Insertar 'Ecuador' en la posición 0
paises.insert(2, 'Perú')  # Insertar 'Perú' en la posición 2
paises.insert(4, 'Brasil')  # Insertar 'Brasil' en la posición 4
print('Lista con nuevos Paises agregados:', paises)

# Ordenar la lista alfabéticamente de manera permanente usando sort()
paises.sort()
print('Paises ordenados:', paises)

# Ordenar la lista alfabéticamente en orden inverso de manera permanente
paises.sort(reverse=True)
print('Paises ordenados al revés:', paises)

# Ordenar la lista temporalmente sin modificarla permanentemente usando sorted()
print('Paises ordenados sin guardar:', sorted(paises))

# Obtener y mostrar la cantidad de países en la lista usando len()
print('Número de paises en la lista:', len(paises))
