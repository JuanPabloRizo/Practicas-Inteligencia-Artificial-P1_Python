# Funciones

# Ejercicio 1: Crear una función que realice una suma
print('***Ejercicio 1***')

# Definición de la función 'suma' que toma dos argumentos y muestra su suma
def suma(numero1, numero2):
    # Imprime el resultado de la suma de 'numero1' y 'numero2'
    print('Resultado suma = ', numero1 + numero2)
    
# Llamadas a la función 'suma' con diferentes pares de números
suma(10, 20)       # Resultado: 30
suma(20, 30)       # Resultado: 50
suma(50000, 7000)  # Resultado: 57000

# Ejercicio 2: Contar el número de argumentos en una función
print('***Ejercicio 2***')

# Definición de la función 'colores' que acepta un número variable de argumentos
def colores(*args):
    # Imprime la cantidad de argumentos pasados a la función
    print('Tiene', len(args), 'Argumentos')

# Llamadas a la función 'colores' con diferentes números de argumentos
colores('rojo', 'azul', 'verde', 'amarillo')  # 4 argumentos
colores('lila', 'negro', 'rojo')               # 3 argumentos
colores('rosa')                                # 1 argumento
colores('marrón', 'naranja')                   # 2 argumentos

# Ejercicio 3: Acceso a argumentos por posición en una función
print('***Ejercicio 3***')

# Definición de la función 'colores' que acepta un número variable de argumentos
def colores(*args):
    # Accede a los argumentos por posición y muestra un mensaje con los colores
    print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

# Llamada a la función 'colores' con dos argumentos
colores('Negro', 'Rojo')  # Imprime los colores en el orden especificado

# Ejercicio 4: Sumar cinco números usando *args
print('***Ejercicio 4***')

# Definición de la función 'suma' que acepta un número variable de argumentos
def suma(*args):
    # Suma los primeros cinco argumentos y muestra el resultado
    resultado = args[0] + args[1] + args[2] + args[3] + args[4]
    print('El resultado de la suma es = ', resultado)

# Llamada a la función 'suma' con cinco argumentos
suma(1, 2, 3, 4, 5)  # Resultado: 15
