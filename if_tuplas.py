# If con Tuplas
# Se define una tupla de colores permitidos
colores = ('verde', 'blanco', 'rojo', 'azul') 
# Se solicita al usuario que ingrese un color
color = input("Introduce un color: ") 

# Se verifica si el color ingresado está dentro de la tupla 'colores'
if color in colores:  
    # Si el color está en la tupla, se imprime que el color está admitido
    print("El color " + color + " está admitido")  
else:  
    # Si el color no está en la tupla, se imprime que no está admitido
    print("Color no admitido")  
