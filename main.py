""" Crear el archivo main del proyecto
    Pedir el nombre del jugador por teclado
    Imprimir un mensaje de bienvenida con el nombre."""

import readchar
import os # importamos la libreria os para usar la funcion clear() y borrar pantalla


def borrar_pantalla ():
    os.system('cls' if os.name == 'nt' else 'clear') # limpiamos la pantalla de la consola

def borrar_imprimir(): 
    if caracter == "n":
        numero = 0
        print("Presione la tecla 'n' para incrementar el numero de 0 - 50" )
        while numero <= 50:
            tecla_n = readchar.readkey() #función que se utiliza para leer una tecla individual desde la entrada estándar 
            if tecla_n == "n":
                borrar_pantalla() # llamamos a la función borrar_pantalla() para borrar la pantalla cada vez que tecleamos n
                numero += 1
                print("Nuevo número:", numero)
            elif tecla_n == "\x1b[A":  # el if valida que la tecla presionada sea UP
                print("Programa finalizado con la tecla UP")
                break


print("Digite el nombre del jugador: ")
nombre = input()
print(f"Hola {nombre}, bienvenido!!")
print("**Presione una tecla para continuar o")
print("presione la tecla UP para finalizar**")


while True:
    caracter = readchar.readkey()   # la variable caracter almacena la tecla presionada.
    print("Tecla presionada: ", caracter) 
    if caracter == "\x1b[A":  # el if valida que la tecla presionada sea UP
        print("Programa finalizado con la tecla UP")
        break
    borrar_imprimir()
   

print("Fin del programa")  







