from jugadores.jugadores import Jugador 
from coordenada import Coordenada
import random as R
from ficha import CIRC,CRUZ,NADA

# LEER UN ENTERO CON CONTROL DE ERROR DE TIPO DE DATO
def leerInt(cartel, desde=-9999999999, hasta=9999999999):
    salir = False
    numero = 0
    while not salir:
        try:
            numero = int(input(cartel))
            if numero < desde or numero > hasta:
                print("ERROR ==> numero fuera de rango\n")
            else:
                salir = True
        except:
            print("ERROR ==> Ingrese un numero entero\n")
    return numero

class Humano(Jugador):
    def __init__(self, nombre, ficha):
        Jugador.__init__(self, nombre, ficha)

    def jugar(self, tablero):
        salir = False
        #Pregunta hasta poner una coordenada vacia
        while not salir:
            columna = leerInt("Columna: ", 1, tablero.cc)
            fila = leerInt("Fila: ", 1, tablero.cf)            
            if tablero.ver(fila-1, columna-1) == NADA:
                salir = True
            else:
                print('Celda ocupada, elija otra.')
        return Coordenada(fila-1, columna-1)