# While con if

# El valor inicial de la variable x será de 0.
x = 0

# Bucle while que se ejecuta mientras x sea menor o igual a 30
while x <= 30:
    # Incrementar el valor de x en 1 en cada iteración
    x += 1  
    
    # Verificar si x es 4, 6 o 10, en cuyo caso se saltará la iteración
    if x == 4 or x == 6 or x == 10:
        # Mensaje que indica que se está saltando estos valores
        print('Se saltó el valor', x, 'de x')
        # Se utiliza 'continue' para saltar a la siguiente iteración del bucle
        continue
    
    # Si x es igual a 15, se rompe el bucle
    if x == 15:
        # Mensaje que indica que el bucle se rompe cuando x vale 15
        print('Bucle While roto debido a que X vale: ', x)
        # Se utiliza 'break' para salir del bucle
        break
    
    # Si no se cumple ninguna de las condiciones anteriores, se imprime el valor actual de x
    print('x= ',x)
