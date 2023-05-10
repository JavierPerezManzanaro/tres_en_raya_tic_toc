#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source 'venv_tic-toc/bin/activate'

#! CUIDADO
# todo por hacer
# ? aviso
# * explicación


import logging
import os
from tabulate import tabulate
import random
from itertools import cycle
from colorama import Fore, init
init(autoreset=True)


# * Configuración de logging
logging.basicConfig(level=logging.WARNING, #WARNING INFO
                    format='-%(levelname)-8s [Línea: %(lineno)-4s Función: %(funcName)-18s] %(message)s')
# logging.debug('Mensaje de traza')
# logging.info('Mensaje Informativo, algo funciona como se espera')
# logging.warning('Peligro')
# logging.error('Error')


# * Variables
grupo_en_orden = []
casillas_ocupadas = []
casillas_X = []
casillas_O = []
jugadas = []
casilla = 0
cadenas_ganadoras = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # horizontales
                     [1, 4, 7], [2, 5, 8], [3, 6, 9], # verticales
                     [1, 5, 9], [3, 5, 7] ] # diagonales
x_color = Fore.GREEN + 'X' + Fore.RESET
o_color = Fore.RED + 'O' + Fore.RESET



def mostrar_tablero(tablero: list):
    """Muestra el tablero con las fichas

    Args:
        tablero (list): lista de las 9 posiciones
    """
    tablero_temp = [
        [pintar_simbolo(tablero[6]), pintar_simbolo(tablero[7]), pintar_simbolo(tablero[8])],
        [pintar_simbolo(tablero[3]), pintar_simbolo(tablero[4]), pintar_simbolo(tablero[5])],
        [pintar_simbolo(tablero[0]), pintar_simbolo(tablero[1]), pintar_simbolo(tablero[2])]
    ]
    print(tabulate(tablero_temp, tablefmt="simple_grid"))


def pintar_simbolo(ficha: str) -> str:
    """Según el contenido de la casilla genera el código de salida:
       el color si es una ficha, si es un número nada y si es una casilla vacia la deja

    Args:
        ficha (str): contenido que va en esa casilla

    Returns:
        str: contenido de la casilla transformado
    """
    simbolo = '·'
    ficha = str(ficha)
    if ficha == 'X':
        simbolo = x_color
    if ficha == 'O':
        simbolo = o_color
    if ficha in '123456789':
        simbolo = ficha
    return simbolo


def ganador(nombre: str):
    """Genera la salida del ganador por el terminal

    Args:
        nombre (str): nombre del ganador
    """
    mensaje = f'*  {nombre} has ganado. ¡¡¡Enhorabuena!!!  *'
    print()
    print()
    print('*'*len(mensaje))
    print(mensaje)
    print('*'*len(mensaje))
    print()


def entrada_casilla(simbolo: str):
    simbolo = x_color if simbolo == 'X' else o_color
    menu_paso = True
    while menu_paso == True:
        try:
            casilla = int(input(f'- {jugador_activo["nombre"]} ¿En que casilla quieres poner tu ficha \'{simbolo}\'? '))
            if casilla <= 0:
                raise casilla_menor_de_1('  No puede ser 0 ni negativo')
            if casilla > 9:
                raise casilla_mayor_de_9('  Tiene que ser un número menor que 9')
            if casilla in casillas_ocupadas:
                raise casilla_ocupada('  Esa casilla ya esta ocupada')
        except ValueError:
            print('  Tienes que introducir un número')
        except casilla_menor_de_1 as e:
            print(e.mensaje)
        except casilla_mayor_de_9 as e:
            print(e.mensaje)
        except casilla_ocupada as e:
            print(e.mensaje)
        else:
            logging.info('La casilla es correcta, seguimos con la app')
            print()
            menu_paso = False
            casillas_ocupadas.append(casilla)
            if jugador_activo["simbolo"] == 'X':
                casillas_X.append(casilla)
            else:
                casillas_O.append(casilla)
        return casillas_X, casillas_O


# * Errores predefinidos para la entrada
class casilla_menor_de_1(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class casilla_mayor_de_9(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class casilla_ocupada(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje



if __name__ == '__main__':

    # * Empezamos la app
    os.system('clear')

    # * Instrucciones
    print('''
Juego del 3 en Raya o del Tic-Toc
---------------------------------

Para colocar la X o O solo es necerario indicar la posición del 1 al 9 dentro del cuadrante
(es el teclado numérico de tu ordenador)
''')

    tablero = [ 1, 2, 3,
                4, 5, 6,
                7, 8, 9 ]
    mostrar_tablero(tablero)
    tablero = ['·', '·', '·',
               '·', '·', '·',
               '·', '·', '·']
    print()
    # * Preguntamos por el nombre de los jugadores
    jugador_1 = input('¿Nombre del jugador que juega con las "' + x_color + '"? ')
    jugador_2 = input('Y ¿nombre del jugador que juega con las "' + o_color + '"? ')
    jugador_1 = {'nombre': jugador_1, 'simbolo': 'X', 'color': 'Fore.GREEN'}
    jugador_2 = {'nombre': jugador_2, 'simbolo': 'O', 'color': 'Fore.RED'}

    print()

    # todo: sección para que el comienzo sea aleatorio
    # comienza = random.randint(1, 2)
    # print(comienza)

    # * Añadimos jugadores y creamos el ciclo de jugadores
    grupo_en_orden.append(jugador_1)
    grupo_en_orden.append(jugador_2)
    grupo_en_orden = cycle(grupo_en_orden)

    # * Ciclo del juego, solo se sale cuando hay un ganador o se empata
    mostrar_tablero(tablero)
    hay_ganador = False
    while hay_ganador == False:
        jugador_activo = next(grupo_en_orden)
        print()

        # * Preguntamos por la casilla y analizamos la entrada
        #casillas_X, casillas_O = entrada_casilla(jugador_activo["simbolo"])
        simbolo = x_color if jugador_activo["simbolo"] == 'X' else o_color
        menu_paso = True
        while menu_paso == True:
            try:
                casilla = int(input(f'- {jugador_activo["nombre"]} ¿En que casilla quieres poner tu ficha \'{simbolo}\'? '))
                if casilla <= 0:
                    raise casilla_menor_de_1('  No puede ser 0 ni negativo')
                if casilla > 9:
                    raise casilla_mayor_de_9('  Tiene que ser un número menor que 9')
                if casilla in casillas_ocupadas:
                    raise casilla_ocupada('  Esa casilla ya esta ocupada')
            except ValueError:
                print('  Tienes que introducir un número')
            except casilla_menor_de_1 as e:
                print(e.mensaje)
            except casilla_mayor_de_9 as e:
                print(e.mensaje)
            except casilla_ocupada as e:
                print(e.mensaje)
            else:
                logging.info('La casilla es correcta, seguimos con la app')
                print()
                menu_paso = False
                casillas_ocupadas.append(casilla)
                casillas_X.append(casilla) if jugador_activo["simbolo"] == 'X' else casillas_O.append(casilla)
                # if jugador_activo["simbolo"] == 'X':
                #     casillas_X.append(casilla)
                # else:
                #     casillas_O.append(casilla)

        logging.info('La app sigue el proceso, ya fuera de la entrada de datos')

        # * Mostramos el tablero con la jugada actual
        tablero[casilla-1] = jugador_activo["simbolo"]
        mostrar_tablero(tablero)
        print()

        # * Empate al no tener huecos libres
        if '·' not in tablero:
            print()
            print('Lo siento, hay un empate')
            print()
            break


        # * Estudiamos si hay ganador
        # * 1) Asignamos las jugadas de cualquiera de los dos a la lista "juganas" que es la que vamos a estudiar
        if jugador_activo["simbolo"] == 'X':
            jugadas = casillas_X
        else:
            jugadas = casillas_O
        # * 2) si el jugador ha dado 3 posiciones
        jugadas.sort()
        if len(jugadas) == 3:
            for cadena_ganadora in cadenas_ganadoras:
                logging.info(f'Con 3 posiciones: {jugadas=}  ||  {cadena_ganadora=}')
                if cadena_ganadora == jugadas:
                    hay_ganador = True
                    ganador(jugador_activo['nombre'])
        # * 3) Y ahora si el jugador ha puesto 4 o más posiciones
        # * Vamos analizando cada una de las posiciones por separado
        if len(jugadas) >= 4:
            for cadena_ganadora in cadenas_ganadoras:
                contador = 0
                logging.info(f'Con 4 posiciones: {jugadas=}  ||  {cadena_ganadora=}')
                for j in cadena_ganadora:
                    for i in jugadas:
                        if(i==j):
                            contador += 1
                            if contador == 3:
                              hay_ganador = True
                              ganador(jugador_activo['nombre'])
                            break

        print()
        print('Fin del juego')
        print()
        print()
