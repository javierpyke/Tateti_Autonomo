from jugadores.jugadores import Jugador 
from coordenada import Coordenada
import random as R
from ficha import CIRC,CRUZ,NADA

class ComputadoraIntermedio(Jugador):
    def __init__(self, nombre, ficha):
        Jugador.__init__(self, nombre, ficha)

    def esTateti(self, tablero, ficha):
        for fila in range(tablero.cf):
            if tablero.filaIgual(fila, ficha):
                return True
        for columna in range(tablero.cc):
            if tablero.columnaIgual(columna, ficha):
                return True
        return tablero.digonalIgual(ficha) or tablero.digonalSecIgual(ficha)
    
    
    def jugar(self, tablero):
        #Se fija si puede rematar el partido
        for f in range(tablero.cf):
            for c in range(tablero.cc):
                if tablero.ver(f, c) == NADA:
                    tablero.poner(f, c, self.ficha)
                    if self.esTateti(tablero, self.ficha):
                        tablero.poner(f, c, NADA)
                        return Coordenada(f, c)
                    else:
                        tablero.poner(f, c, NADA)

        #Toma la ficha del oponente
        if self.ficha == CIRC:
            otra = CRUZ
        else:
            otra = CIRC        
        
        #Se fija si puede perder el partido en la siguiente mano
        for f in range(tablero.cf):
            for c in range(tablero.cc):
                if tablero.ver(f, c) == NADA:
                    tablero.poner(f, c, otra)
                    if self.esTateti(tablero, otra):
                        tablero.poner(f, c, NADA)
                        # Tapa la posibilidad del oponente
                        return Coordenada(f, c)
                    else:
                        tablero.poner(f, c, NADA)

        #Juga random
        salir = False
        fila = 0
        columna = 0        
        while not salir:
            fila = R.randint(0, tablero.cf-1)
            columna = R.randint(0, tablero.cc-1)
            if tablero.ver(fila, columna) == NADA:
                salir = True
        return Coordenada(fila, columna)