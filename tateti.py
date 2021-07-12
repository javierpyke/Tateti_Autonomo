from tablero import Tablero
from ficha import Ficha,CRUZ,CIRC,NADA
import random as R

class Tateti:
    def __init__(self, jug1, jug2):        
        self.jug1 = jug1
        self.jug2 = jug2
        self.tablero = Tablero()

    def jugarTateti(self):
        # Aleatorio quien empieza
        if R.randint(0, 1) == 0:
            jugAct = self.jug1
        else:
            jugAct = self.jug2
        ganar = False
        print(str(self.tablero))
        # Se juega mientras no haya ganador y haya un lugar libre
        while not ganar and self.tablero.existe(NADA):
            print("JUEGA: " + str(jugAct))
            coor = jugAct.jugar(self.tablero)
            # Pone la ficha en el tablero
            self.tablero.poner(coor.fila, coor.columna, jugAct.ficha)
            print(str(self.tablero))
            #Se fija si hubo TATETI
            if self.esTateti(jugAct.ficha):
                ganar = True
            #En caso que no cambia de jugador
            else:
                jugAct = self.elOtroJugador(jugAct) 
        #Si hubo ganador lo muestra por pantalla y lo devulve
        if ganar:
            print("Ganador: " + str(jugAct))
            return jugAct
        #En caso de empate lo muestra y devuelve False
        else:
            print("EMPATE")
        return False

    def elOtroJugador(self, unJugador):
        # Dependiendo cual sea el jugador actual devuelve el contrario        
        if unJugador == self.jug2:
            return self.jug1
        return self.jug2

    def esTateti(self, ficha):     
        # Recorre las filas y se fija si en alguna hay TATETI   
        for fila in range(self.tablero.cf):
            if self.tablero.filaIgual(fila, ficha):
                return True        
        # Recorre las columnas y se fija si en alguna hay TATETI   
        for columna in range(self.tablero.cc):
            if self.tablero.columnaIgual(columna, ficha):
                return True
        # Se fija si hay TATETI en la diagonal principal
        if self.tablero.digonalIgual(ficha):
            return True
        # Se fija si hay TATETI en la diagonal secundaria
        if self.tablero.digonalSecIgual(ficha):
            return True
        
        return  False