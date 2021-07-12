from jugadores.jugadores import Jugador 
from coordenada import Coordenada
import random as R
from ficha import CIRC,CRUZ,NADA

class ComputadoraFacil(Jugador):

    def __init__(self, nombre, ficha):
        super().__init__(nombre, ficha)
    
    def jugar(self, tablero):
        salir = False
        while not salir:
            fila = R.randint(0, tablero.cf-1)
            columna = R.randint(0, tablero.cc-1)
            if tablero.ver(fila, columna) == NADA:
                salir = True
        return Coordenada(fila, columna)