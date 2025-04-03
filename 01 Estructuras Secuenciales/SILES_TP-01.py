#Alumno Cristian siles  DNI: 39959371
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# # 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# # el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# # por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# # realizar la impresión por pantalla.
nombre = input("Por favor ingrese su nombre : ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla

nombre = input("Por favor ingrese su nombre : ")
apellido = input("Por favor ingrese su apellido : ")
edad = input("Por favor ingrese su edad : ")
lugar_residencia = input("Por favor ingrese su Lugar de Residencia : ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float(input("Por ingrese el radio de un circulo : "))
pi = 3.14159
area = pi *radio*radio
perimetro = 2 * pi * radio
print(f"El area del circulo es : {area} y su perimetro es : {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Por favor ingrese una cantidad de segundos : "))
horas_equivalentes = (segundos / 60 )
print(f"{segundos} segundos equivalen a {horas_equivalentes} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero_ejercicio_6 = int(input("Por favor ingrese un numero : "))
print(f"{numero_ejercicio_6} x 1 = {numero_ejercicio_6 * 1}")
print(f"{numero_ejercicio_6} x 2 = {numero_ejercicio_6 * 2}")
print(f"{numero_ejercicio_6} x 3 = {numero_ejercicio_6 * 3}")
print(f"{numero_ejercicio_6} x 4 = {numero_ejercicio_6 * 4}")
print(f"{numero_ejercicio_6} x 5 = {numero_ejercicio_6 * 5}")
print(f"{numero_ejercicio_6} x 6 = {numero_ejercicio_6 * 6}")
print(f"{numero_ejercicio_6} x 7 = {numero_ejercicio_6 * 7}")
print(f"{numero_ejercicio_6} x 8 = {numero_ejercicio_6 * 8}")
print(f"{numero_ejercicio_6} x 9 = {numero_ejercicio_6 * 9}")
print(f"{numero_ejercicio_6} x 10 = {numero_ejercicio_6 * 10}")

# for i in range(1, 11):  
#     resultado = numero_ejercicio_6 * i
#     print(f"{numero_ejercicio_6} x {i} = {resultado}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_1_ejercicio_7 = int(input("Por favor ingrese un numero distinto de 0 : "))
numero_2_ejercicio_7 = int(input("Por favor ingrese un Segundo numero distinto de 0: "))
suma = numero_1_ejercicio_7 + numero_2_ejercicio_7
division = float(numero_1_ejercicio_7 / numero_2_ejercicio_7)
multiplicacion = numero_1_ejercicio_7 * numero_2_ejercicio_7
resta = numero_1_ejercicio_7 - numero_2_ejercicio_7
print(f"El resultado de sumar {numero_1_ejercicio_7} + {numero_2_ejercicio_7} es : {suma} ")
print(f"El resultado de dividirlos es : {division} ")
print(f"El resultado de multiplicarlos es : {multiplicacion} ")
print(f"El resultado de restarlos es : {resta} ")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:  IMC = peso en kg / (altura en m) al cuadrado

altura = float(input("Por favor ingrese su altura en metros: "))
peso = float(input("Por favor ingrese su Peso en kilogramos: "))
imc = peso /(altura)**2
print(f"Tu indice de masa corporal es : {imc} ")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# temperatura en fahrenheit = 9/5 . temperatura en celcius + 32

temperatura_celsius = int(input("Por favor ingrese una temperatura en grados Celsius: "))
temperatura_Fahrenheit = temperatura_celsius * (9/5) + 32
print(f"La temperatura equivalente en grados Fahrenheit son : {temperatura_Fahrenheit} grados Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

numero_1_ejercicio_10 = int(input("Por favor ingrese un numero : "))
numero_2_ejercicio_10 = int(input("Por favor ingrese un Segundo numero : "))
numero_3_ejercicio_10 = int(input("Por favor ingrese un Tercer numero : "))

promedio = (numero_1_ejercicio_10 + numero_2_ejercicio_10 + numero_3_ejercicio_10) / 3

print(f"El promedio de los 3 numeros ingresados es : {promedio}")