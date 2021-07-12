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
        #ATACAR (REMATE)
        for f in range(tablero.cf):
            for c in range(tablero.cc):
                if tablero.ver(f, c) == NADA:
                    tablero.poner(f, c, self.ficha)
                    if self.esTateti(tablero, self.ficha):
                        tablero.poner(f, c, NADA)
                        return Coordenada(f, c)#ACA GANO!!!
                    else:
                        tablero.poner(f, c, NADA)

        #TOMO LA FICHA DEL OPONENTE
        if self.ficha == CIRC:
            otra = CRUZ
        else:
            otra = CIRC        
        
        #DEFENDER
        for f in range(tablero.cf):
            for c in range(tablero.cc):
                if tablero.ver(f, c) == NADA:
                    tablero.poner(f, c, otra)
                    if self.esTateti(tablero, otra):
                        tablero.poner(f, c, NADA)
                        return Coordenada(f, c)#TAPO LA POSIBILIDAD DE QUE GANE
                    else:
                        tablero.poner(f, c, NADA)
        salir = False
        fila = 0
        columna = 0

        #JUEGA RANDOM
        while not salir:
            fila = R.randint(0, tablero.cf-1)
            columna = R.randint(0, tablero.cc-1)
            if tablero.ver(fila, columna) == NADA:
                salir = True
        return Coordenada(fila, columna)