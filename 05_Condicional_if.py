#Ejercicios IF

#Cambia el operador para que la condición sea True.
    #num1 = 15
    #num2 = 20
    #if num1 == num2:
num1 = 15
num2 = 20
if num1 != num2:
    print('Se ejecuta el if 1.')
#Cambia el operador para que la condición sea True.
#num1 = 1450
#num2 = 60
#if num1 < num2:
num1 = 1450
num2 = 60
if num1 > num2:
	print('Se ejecuta el if 2.')
# Haz que el siguiente condicional se convierta en False sin cambiar el operador.
#num1 = 1450
#num2 = 60
#if num1 != num2:
num1 = 1450
num2 = 60
if num1 == num2:
	print('Se ejecuta el if 3.')

#Ejercicio if else
      
#Corrige el siguiente condicional if else.
#color = rojo
#else color == rojo
#Print "El color es rojo."
#if color != rojo
#Print "El color no es rojo."
color = "rojo"
if color == "rojo":  
    print("El color es rojo.") 
else:
    print("El color no es rojo.") 

#Ejercicio if elif else
edad = int(input("Ingrese su Edad = "))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres un adulto joven')
elif edad >45 and edad <= 100:
	print('Eres un adulto mayor.')
elif edad >100 and edad <= 120:
	print("Eres de edad muy avanzada")
else:   
	print('Edad no válida.')
