# Strings y variables
mensaje = "Practicas Primer parcial del grupo"  # Se asigna una cadena de texto a la variable 'mensaje'
grupo = 6  # Se asigna el valor entero 6 a la variable 'grupo'
print (mensaje, grupo, 'E')  # Se imprime el mensaje, el número de grupo, y la letra 'E'

nombre = 'Juan Pablo '  # Se asigna la cadena de texto 'Juan Pablo ' a la variable 'nombre'
apellidos = 'Rizo Riestra'  # Se asigna la cadena 'Rizo Riestra' a la variable 'apellidos'
completo = nombre + apellidos  # Se concatenan las variables 'nombre' y 'apellidos' en la variable 'completo'
print ('De ' + completo + ' 22110371')  # Se imprime una cadena con la variable 'completo' y el número 22110371

# Métodos y saltos de línea y tabulaciones
titulo = 'inteligencia artificial'  # Se asigna la cadena 'inteligencia artificial' a la variable 'titulo'
titulo = titulo.upper()  # Se convierte el texto de 'titulo' a mayúsculas usando el método upper()

nombre = 'mauricio alejandro cabrera arellano'  # Se asigna el nombre en minúsculas a la variable 'nombre'
nombre = nombre.title()  # Se convierte cada palabra de 'nombre' para que comience con mayúscula usando title()

profesor = 'PROFESOR:'  # Se asigna la cadena 'PROFESOR:' a la variable 'profesor'
print (titulo + '\n' + profesor.lower() + '\t' + nombre)  # Se imprime el título en mayúsculas, 
                                                          # seguido de un salto de línea ('\n'), el texto 'profesor' en minúsculas,
                                                          # luego una tabulación ('\t') y finalmente el nombre con mayúscula inicial en cada palabra
