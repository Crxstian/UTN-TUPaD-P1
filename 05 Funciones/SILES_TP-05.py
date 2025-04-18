# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#  2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario(input("Por favor ingrese un nombre "))

#  3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados

def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)

#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
pi = 3.14159
def calcular_area_circulo(radio):
    return pi *radio*radio

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio = float(input("Por ingrese el radio de un circulo : "))
print(f"El area del circulo es : {calcular_area_circulo(radio):.2f}, y su perimetro es {calcular_perimetro_circulo(radio):.2f}")

#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Por ingrese los segundos para pasar a horas : "))
print(f"{segundos} Segunos equivalen a {segundos_a_horas(segundos):.2f} Horas")


#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

def tabla_multiplicar(numero):
    for i in range (0,11):
        print(f"{numero} x {i} = {numero*i}")

numero_imprimir_tabla = int(input("Por ingrese un numero para mostrar su tabla de multiplicacion : "))
tabla_multiplicar(numero_imprimir_tabla)


#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b

numero_a = int(input("Por ingrese un numero : "))
numero_b = int(input("Por ingrese otro numero : "))
suma, resta, multiplicacion, division = operaciones_basicas(numero_a, numero_b)
# print(f"El resultado de las operaciones basicas entre los 2 numeros ingresados son: Suma: {operaciones_basicas(numero_a,numero_b)[0]}, Resta: {operaciones_basicas(numero_a,numero_b)[1]}, Multiplicacion: {operaciones_basicas(numero_a,numero_b)[2]}, Division: {operaciones_basicas(numero_a,numero_b)[3]}")
print(f"Resultados de las operaciones básicas:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso /(altura)**2

peso = float(input("Por favor ingrese su Peso en kilogramos: ")) 
altura = float(input("Por favor ingrese su altura en metros: "))
print(f"Tu indice de masa corporal es : {calcular_imc(peso,altura):.2f} ")

#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return celsius * (9/5) + 32

temperatura_celsius = int(input("Por favor ingrese una temperatura en grados Celsius: "))
print(f"La temperatura equivalente en grados Fahrenheit son : {celsius_a_fahrenheit(temperatura_celsius)} grados Fahrenheit")

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

def calcular_promedio(a, b, c):
    return (a+b+c)/3

numero_a_ej10 = int(input("Por ingrese un numero : "))
numero_b_ej10 = int(input("Por ingrese otro numero : "))
numero_c_ej10 = int(input("Por ingrese otro numero : "))
print(f"El promedio de los 3 numeros ingresados es: {calcular_promedio(numero_a_ej10,numero_b_ej10,numero_c_ej10):.2f}")