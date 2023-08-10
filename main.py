""" Crear el archivo main del proyecto
    Pedir el nombre del jugador por teclado
    Imprimir un mensaje de bienvenida con el nombre."""

import readchar

print("Digite el nombre del jugador: ")
nombre = input()
print(f"Hola {nombre}, bienvenido!!")
print("**Presione una tecla para continuar y")
print("presione la tecla UP para finalizar**")


while True:
    caracter = readchar.readkey()   # la variable caracter almacena la tecla presionada.
    print("Tecla presionada: ", caracter) 
    if readchar.readkey() == "\x1b[A": # el if valida que la tecla presionada sea UP
        print("Programa finalizado con la tecla UP")
        break