# Tuplas y Listas
listapaises = ['Ecuador', 'Colombia', 'Perú', 'Chile', 'Venezuela']  # Definir una lista de países
tuplaspaises = ('México', 'Estados Unidos', 'Canadá', 'Argentina', 'Brasil')  # Definir una tupla de países (inmutable)
print('Lista', listapaises, '\n', 'Tupla', tuplaspaises)  # Imprimir la lista y la tupla

# Crear una tupla de números del 1 al 10
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  

# Realizar una suma con los elementos en la posición 0 y 2 de la tupla de números
Resultado = numeros[0] + numeros[2]  
print('El país', tuplaspaises[0], 'tiene', Resultado, 'Goles')  # Imprimir un mensaje con el resultado de la suma

# Realizar una resta con los elementos en la posición 9 y 4 de la tupla de números
Resultado = numeros[9] - numeros[4]
print('El país', tuplaspaises[3], 'tiene', Resultado, 'Goles')  # Imprimir otro mensaje con el resultado de la resta

# Convertir la lista de países en una tupla
nuevatupla = tuple(listapaises)
# Convertir la tupla de países en una lista
nuevalista = list(tuplaspaises)
print('Nueva Tupla', nuevatupla, '\n', 'Nueva Lista', nuevalista)  # Imprimir la nueva tupla y la nueva lista

