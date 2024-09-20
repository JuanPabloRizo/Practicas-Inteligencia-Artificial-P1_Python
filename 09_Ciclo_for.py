# Ejercicios con for

# Ejercicio 1
# Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración:
# 'El color es: ' + color + '.'.
colores = ('rojo','azul','verde','amarillo')

print("***Ejercicio 1***")
# Iteramos sobre la tupla de colores
for x in colores:
    # En cada iteración se imprime el color correspondiente con el mensaje formateado
    print('El color es: ' + x + '.')

# Ejercicio 2
# Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. 
# Basta con que imprimas el valor de cada iteración.

print("\n***Ejercicio 2***")
# El bucle for usa range() para generar una secuencia desde 7 hasta 700 con saltos de 100
for x in range(7, 700, 100):
    # Se imprime cada valor de la secuencia generada por el range()
    print(x)
