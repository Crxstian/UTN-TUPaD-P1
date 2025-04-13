# Actividades 
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range(101):
    print (i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

numero_usuario = int(input("Por favor ingrese un numero entero: "))
cantidad_digitos = 0
while numero_usuario > 0:
    numero_usuario //=10
    cantidad_digitos +=1
print("La cantida de digitos es: ",cantidad_digitos)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 
numero_usuario_1 = int(input("Por favor ingrese un numero entero: "))
numero_usuario_2 = int(input("Por favor ingrese otro numero entero: "))
sumatoria = 0
for i in range(numero_usuario_1 +1, numero_usuario_2,1):
    sumatoria +=i
print("La sumatoria entre los dos valores ingresados es : ",sumatoria)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 
numero_usuario_ej4 = int(input("Por favor ingrese un numero entero: "))
sumatoria_ej4 = numero_usuario_ej4
while numero_usuario_ej4 !=0:
    numero_usuario_ej4 = int(input("Por favor ingrese un numero entero: "))
    sumatoria_ej4 +=numero_usuario_ej4
print("El total acumulado en sumatoria es : ",sumatoria_ej4)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
# import random

numero_aleatorio = random.randint(0,9)
intentos = 1
numero_intento = int(input("Por favor ingrese un número entero aleatorio entre 0 y 9: "))
while numero_intento != numero_aleatorio:
    intentos +=1
    numero_intento = int(input("Por favor ingrese un número entero aleatorio entre 0 y 9: "))
print("Adivinaste el numero!!")
print("Los intentos fueron necesarios para acertar el número fueron : ",intentos)



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

print("Imprimiendo todos los números pares comprendidos entre 0 y 100, en orden decreciente: ")

for i in range(100,-1,-1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

numero_usuario_ej7 = int(input("Por favor ingrese un numero entero positivo: "))
sumatoria_ej7 = 0
for i in range (0,numero_usuario_ej7+1,1):
    sumatoria_ej7 += i
print("La sumatoria entre 0 y el valor ingresado es : ",sumatoria_ej7)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

contador_ej8 = 0
cantidad_pares = 0
cantidad_impares = 0
cantidad_positivos = 0
cantidad_negativos = 0

while contador_ej8 != 100:
    numero_usuario_ej8 = int(input("Por favor ingrese un numero entero: "))
    contador_ej8 +=1
    if numero_usuario_ej8 % 2 ==0:
        cantidad_pares +=1
    else:
        cantidad_impares +=1
    if numero_usuario_ej8 >=0:
        cantidad_positivos +=1
    else:
        cantidad_negativos +=1

print("La cantidad de numeros pares es: ",cantidad_pares)
print("La cantidad de numeros impares es: ",cantidad_impares)
print("La cantidad de numeros positivos es: ", cantidad_positivos)
print("La cantidad de numeros negativos es: ", cantidad_negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

promedio = 0
contador_ej9 = 0
sumatoria_ej9 = 0
while contador_ej9 !=100:
    numero_usuario_ej9 = int(input("Por favor ingrese un numero entero: "))
    contador_ej9 +=1
    sumatoria_ej9 += numero_usuario_ej9

promedio = sumatoria_ej9 / contador_ej9
print("La media de los valores ingresados es: ",promedio)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

numero_usuario_ej10 = int(input("Por favor ingrese un numero entero: "))
numero_invertido = 0

while numero_usuario_ej10 > 0:
    digito = numero_usuario_ej10 % 10
    numero_invertido = numero_invertido * 10 + digito
    numero_usuario_ej10 = numero_usuario_ej10 // 10

print("El número invertido es:", numero_invertido)