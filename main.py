from tablero import Tablero
from ficha import Ficha,CRUZ,CIRC,NADA
from coordenada import Coordenada
from jugadores.computadora_dificil import ComputadoraDificil
from jugadores.computadora_intermedio import ComputadoraIntermedio
from jugadores.computadora_facil import ComputadoraFacil
from jugadores.humano import Humano
from tateti import Tateti
import random as R

def elegir_opcion():
    eleccion=0
    while eleccion < 1 or eleccion > 4:
        try:
            eleccion = int(input("""¿Que tipo de jugador quiere ser:
                [1]: Computadora facil
                [2]: Computadora intermedio
                [3]: Computadora dificil
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
    nombre=""
    opcion = elegir_opcion()
    if opcion == 4:
        nombre = elegir_nombre()
    ficha = elegir_ficha(jug1)
    lst_nombres = ["Computadora Facil","Computadora Intermedio","Computadora Dicifil",nombre]
    return lst_jugadores[opcion-1](lst_nombres[opcion-1],ficha)

def main():
    jug1 = elegir_jugador()
    print(jug1)
    jug2 = elegir_jugador(jug1)
    print(jug2)
    juego = Tateti(jug1, jug2)
    juego.jugarTateti()  


if __name__ == '__main__':
    main()
