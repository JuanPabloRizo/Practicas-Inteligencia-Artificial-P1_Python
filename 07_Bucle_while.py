# Ejercicios con while

# Ejercicio 1: Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
print("***Ejercicio 1***")
x = 0  # Inicializa la variable x con valor 0
while x <= 15:  # El bucle se ejecuta mientras x sea menor o igual a 15
    print(x)  # Imprime el valor actual de x
    x += 5  # Incrementa x en 5 en cada iteración

# Ejercicio 2: Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
print("***Ejercicio 2***")
x = 0  # Inicializa la variable x con valor 0
while x >= -100:  # El bucle se ejecuta mientras x sea mayor o igual a -100
    print(x)  # Imprime el valor actual de x
    x -= 20  # Decrementa x en 20 en cada iteración

# Ejercicio 3: Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1.
# Muestra en cada ejecución: 'El valor del bucle es {x}'.
print("***Ejercicio 3***")
x = 10  # Inicializa la variable x con valor 10
while x >= 0:  # El bucle se ejecuta mientras x sea mayor o igual a 0
    print('El valor del bucle es ' + str(x))  # Imprime el valor actual de x dentro del mensaje
    x -= 1  # Decrementa x en 1 en cada iteración
