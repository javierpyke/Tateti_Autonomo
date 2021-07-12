from tablero import Tablero
from ficha import Ficha,CRUZ,CIRC,NADA
from coordenada import Coordenada
from jugadores.computadora_dificil import ComputadoraDificil
from jugadores.computadora_intermedio import ComputadoraIntermedio
from jugadores.computadora_facil import ComputadoraFacil
from jugadores.humano import Humano

import random as R

class Tateti:
    def __init__(self, jug1, jug2):        
        self.jug1 = jug1
        self.jug2 = jug2
        self.tablero = Tablero()

    def jugarTateti(self):
        if R.randint(0, 1) == 0:
            jugAux = self.jug1
        else:
            jugAux = self.jug2
        ganar = False
        print(str(self.tablero))
        while not ganar and self.tablero.existe(NADA):
            print("JUEGA: " + str(jugAux))
            coor = jugAux.jugar(self.tablero)
            self.tablero.poner(coor.fila, coor.columna, jugAux.ficha)
            print(str(self.tablero))
            if self.esTateti(jugAux.ficha):
                ganar = True
            else:
                jugAux = self.elOtroJugador(jugAux) 
        if ganar:
            print("Ganador: " + str(jugAux))
            return jugAux
        else:
            print("EMPATE")
        return False

    def elOtroJugador(self, unJugador):
        
        if unJugador == self.jug2:
            return self.jug1
        return self.jug2

    def esTateti(self, ficha):
        
        for fila in range(self.tablero.cf):
            if self.tablero.filaIgual(fila, ficha):
                return True
        
        for columna in range(self.tablero.cc):
            if self.tablero.columnaIgual(columna, ficha):
                return True
        
        if self.tablero.digonalIgual(ficha):
            return True

        if self.tablero.digonalSecIgual(ficha):
            return True
        
        return  False

def elegir_opcion():
    eleccion=0
    while eleccion < 1 or eleccion > 4:
        try:
            eleccion = int(input("""¿Que tipo de jugador quiere ser:
                [1]: Computadora facil
                [2]: Computadora intermedio
                [3]: Computadora dificl
                [4]: Humano
                Ingrese una opcion: """))
                                                                
        except:
                print("ERROR ==> Ingrese un numero entero\n")
        if eleccion < 1 or eleccion > 4:
            print('ERROR ==> Ingrese un numero de la lista')
    return eleccion

def elegir_nombre():
    return input("Ingrese su nombre: ")

def elegir_ficha(jug1):
    if jug1:
        if jug1.ficha == CRUZ:
            return CIRC
        else:
            return CRUZ
    else:
        opcion = ''
        while opcion.upper() != 'X' and opcion.upper() != 'O':
            opcion = input('Ingrese que ficha quiere X o O: ')
        if opcion.upper() == 'X':
            return CRUZ
        else:
            return CIRC

def elegir_jugador(jug1=None):
    lst_jugadores = [ComputadoraFacil,ComputadoraIntermedio,ComputadoraDificil,Humano]
    opcion = elegir_opcion()
    nombre = elegir_nombre()
    ficha = elegir_ficha(jug1)
    return lst_jugadores[opcion-1](nombre,ficha)

def main():
    '''jug1 = elegir_jugador()
    print(jug1)
    jug2 = elegir_jugador(jug1)
    print(jug2)'''

    jug1 = ComputadoraIntermedio("Xompu 2",CIRC)
    jug2 = ComputadoraDificil("Xompu 3",CRUZ)
    

    puntos1 = 0
    puntos2 = 0

    for x in range(50):
        juego = Tateti(jug1, jug2)
        ganador = juego.jugarTateti()
        if ganador == jug1:
            puntos1 +=1
        elif ganador == jug2:
            puntos2 += 1
    print("{}: {}".format(jug1.nombre,puntos1))
    print("{}: {}".format(jug2.nombre,puntos2))

    jug1 = ComputadoraFacil("Xompu 1",CIRC)
    jug2 = ComputadoraDificil("Xompu 3",CRUZ)

    for x in range(50):
        juego = Tateti(jug1, jug2)
        ganador = juego.jugarTateti()
        if ganador == jug1:
            puntos1 +=1
        elif ganador == jug2:
            puntos2 += 1
    print("{}: {}".format(jug1.nombre,puntos1))
    print("{}: {}".format(jug2.nombre,puntos2))


if __name__ == '__main__':
    main()
