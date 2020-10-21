
import random as R
"""import os
from time import sleep"""

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
# -------------------------------------------------------------------------
class Ficha:
    def __init__(self, caracter):
        self.caracter = caracter

    def __str__(self):
        return '['+self.caracter+']'
 
CRUZ = Ficha('X')
CIRC = Ficha('O')
NADA = Ficha(' ')
# -------------------------------------------------------------------------
class Tablero:
    
    def __init__(self, filas=3, columnas=3):
        self.cf = filas
        self.cc = columnas
        self.mat = []
        
        for f in range(self.cf):
            col = []
            for c in range(self.cc):
                col.append(NADA)
            self.mat.append(col)

    def primera_fila(self):
        return 0
    def primera_columna(self):
        return 0
    def ultima_fila(self):
        return self.cf-1
    def ultima_columna(self):
        return self.cc-1
    def __str__(self):
        cadena = ""
        for f in range(self.cf):
            for c in range(self.cc):
                cadena += str(self.mat[f][c])
            cadena += "\n"
        return cadena

    def poner(self, f, c, ficha):
        self.mat[f][c] = ficha

    def ver(self, f, c):
        return self.mat[f][c]

    def existe(self, ficha):
        for f in range(self.cf):
            for c in range(self.cc):
                if ficha == self.mat[f][c]:
                    return True
        return False

    def filaIgual(self, fila, ficha):
        for c in range(self.cc):
            if ficha != self.mat[fila][c]:
                return False
        return True

    def columnaIgual(self, columna, ficha):
        for f in range(self.cf):
            if ficha != self.mat[f][columna]:
                return False
        return True

    def digonalIgual(self, ficha):
        for x in range(self.cf):
            if self.mat[x][x] != ficha:
                return False
        return True

    def digonalSecIgual(self, ficha):
        f = 0
        c = self.cc-1
        while f < self.cf:
            if self.mat[f][c] != ficha:
                return False
            f += 1
            c -= 1
        return True
# -------------------------------------------------------------------------
class Jugador(object):
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def __str__(self):
        return self.nombre + " ==> "+str(self.ficha)

    def jugar(self, tablero):
        pass
# -------------------------------------------------------------------------
class Humano(Jugador):
    def __init__(self, nombre, ficha):
        Jugador.__init__(self, nombre, ficha)

    def jugar(self, tablero):
        salir = False
        while not salir:
            columna = leerInt("Columna: ", 1, tablero.cc)
            fila = leerInt("Fila: ", 1, tablero.cf)            
            if tablero.ver(fila-1, columna-1) == NADA:
                salir = True
            else:
                print('Celda ocupada, elija otra.')
        return Coordenada(fila-1, columna-1)
# -------------------------------------------------------------------------
class Computadora_nivel0(Jugador):
    # def __init__(self, nombre, ficha):
    #     Jugador.__init__(self, nombre, ficha)

    def __init__(self, nombre, ficha):
        super().__init__(nombre, ficha)
    
    def jugar(self, tablero):
        """sleep(1) # Time in seconds."""
        salir = False
        while not salir:
            fila = R.randint(0, tablero.cf-1)
            columna = R.randint(0, tablero.cc-1)
            if tablero.ver(fila, columna) == NADA:
                salir = True
        return Coordenada(fila, columna)

# -------------------------------------------------------------------------


class Computadora_nivel1(Jugador):
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
        """sleep(2) # Time in seconds."""
        
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

class Computadora_nivel3(Jugador):
    
    def __init__(self, nombre, ficha, primer_jugador=False, jugadas=0):
        super().__init__(nombre=nombre, ficha=ficha)
        self.primer_jugador = primer_jugador
        self.jugadas = jugadas
    
    def atacar_filas(self,tablero):
        fila = tablero.primera_fila()
        while fila <= tablero.ultima_fila():
            coordenada = self.atacar_fila(fila,tablero)
            if coordenada != False:
                return coordenada
            fila +=1
        return False  

    def atacar_fila(self,fila,tablero):
        fichas = 0
        lugar_vacio = 0
        c = tablero.primera_columna()
        while c <= tablero.ultima_columna():
            if tablero.ver(fila,c) == self.ficha:
                fichas += 1
            elif tablero.ver(fila,c) == NADA:
                lugar_vacio +=1
                coordenada = Coordenada(fila,c) 
            c += 1
        if fichas == 2 and lugar_vacio == 1:
            return coordenada                                                            # NADA
        return False
    
    def atacar_columnas(self,tablero):
        columna = tablero.primera_columna()
        while columna <= tablero.ultima_columna():
            coordenada = self.atacar_columna(columna,tablero)
            if coordenada != False:
                return coordenada
            columna +=1
        return False

    def atacar_columna(self,columna,tablero):
        fichas = 0
        lugar_vacio = 0
        f = tablero.primera_fila()
        while f <= tablero.ultima_fila():
            if tablero.ver(f,columna) == self.ficha:
                fichas += 1
            elif tablero.ver(f,columna) == NADA:
                lugar_vacio +=1
                coordenada = Coordenada(f,columna) 
            f += 1
        if fichas == 2 and lugar_vacio == 1:
            return coordenada                                                            # NADA
        return False

    def atacar_diagonales(self,tablero):
        coor = self.atacar_diagonal_principal(tablero)
        if coor != False:
            return coor
        coor = self.atacar_diagonal_secundario(tablero)
        if coor != False:
            return coor
        return False

    def atacar_diagonal_principal(self,tablero):
        fichas = 0
        lugar_vacio = 0
        x = tablero.primera_fila()
        while x <= tablero.ultima_fila():
            if tablero.ver(x,x) == self.ficha:
                fichas += 1
            elif tablero.ver(x,x) == NADA:
                lugar_vacio +=1
                coordenada = Coordenada(x,x)
            x += 1
        if fichas == 2 and lugar_vacio == 1:
            return coordenada
        return False

    def atacar_diagonal_secundario(self,tablero):
        fichas = 0
        lugar_vacio = 0
        f = tablero.primera_fila()
        c = tablero.ultima_columna()        
        while f <= tablero.ultima_fila():
            if tablero.ver(f,c) == self.ficha:
                fichas += 1
            elif tablero.ver(f,c) == NADA:
                lugar_vacio +=1
                coordenada = Coordenada(f,c)
            f = f + 1
            c = c - 1
        if fichas == 2 and lugar_vacio == 1:
            return coordenada
        return False

    def defender(self,tablero):
        coor = self.defender_filas(tablero)
        if coor != False:
            print("ok1")
            return coor
        coor = self.defender_columnas(tablero)
        if coor != False:
            print("ok2")
            return coor
        coor = self.defender_diagonales(tablero)
        if coor != False:
            print("ok3")
            return coor
        return False
    
    def defender_filas(self,tablero):
        fila = tablero.primera_fila()
        while fila <= tablero.ultima_fila():
            coordenada = self.defender_fila(fila,tablero)
            if coordenada != False:
                return coordenada
            fila +=1
        return False  

    def defender_fila(self,fila,tablero):
        fichas = 0
        lugar_vacio = 0
        c = tablero.primera_columna()
        while c <= tablero.ultima_columna():
            if tablero.ver(fila,c) == NADA:
                lugar_vacio +=1
                coordenada = Coordenada(fila,c)
            elif tablero.ver(fila,c) != self.ficha:
                fichas += 1
            c += 1
        if fichas == 2 and lugar_vacio == 1:
            return coordenada                                                            # NADA
        return False
    
    def defender_columnas(self,tablero):
        columna = tablero.primera_columna()
        while columna <= tablero.ultima_columna():
            coordenada = self.defender_columna(columna,tablero)
            if coordenada != False:
                return coordenada
            columna +=1
        return False

    def defender_columna(self,columna,tablero):
        fichas = 0
        lugar_vacio = 0
        f = tablero.primera_fila()
        while f <= tablero.ultima_fila():
            if tablero.ver(f,columna) == NADA:
                lugar_vacio +=1
                coordenada = Coordenada(f,columna) 
            elif tablero.ver(f,columna) != self.ficha:
                fichas += 1
            f += 1
        if fichas == 2 and lugar_vacio == 1:
            return coordenada                                                            # NADA
        return False

    def defender_diagonales(self,tablero):
        coor = self.defender_diagonal_principal(tablero)
        if coor != False:
            return coor
        coor = self.defender_diagonal_secundario(tablero)
        if coor != False:
            return coor
        return False

    def defender_diagonal_principal(self,tablero):
        fichas = 0
        lugar_vacio = 0
        x = tablero.primera_fila()
        while x <= tablero.ultima_fila():
            if tablero.ver(x,x) == NADA:
                lugar_vacio +=1
                coordenada = Coordenada(x,x)
            elif tablero.ver(x,x) != self.ficha:
                fichas += 1            
            x += 1
        if fichas == 2 and lugar_vacio == 1:
            return coordenada
        return False

    def defender_diagonal_secundario(self,tablero):
        fichas = 0
        lugar_vacio = 0
        f = tablero.primera_fila()
        c = tablero.ultima_columna()        
        while f <= tablero.ultima_fila():
            if tablero.ver(f,c) == NADA:
                lugar_vacio +=1
                coordenada = Coordenada(f,c)
            elif tablero.ver(f,c) != self.ficha:
                fichas += 1            
            f = f + 1
            c = c - 1
        if fichas == 2 and lugar_vacio == 1:
            return coordenada
        return False

    def es_primer_jugador(self,tablero):
        for f in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            for c in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                if tablero.ver(f,c) != NADA:
                    return False
        return True

    def posible_tateti_columna(self,tablero,columna):
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            if tablero.ver(fila,columna) != NADA and tablero.ver(fila,columna) != self.ficha:
                return False
        return True

    def posible_tateti_fila(self,tablero,fila):
        for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
            if tablero.ver(fila,columna) != NADA and tablero.ver(fila,columna) != self.ficha:
                return False
        return True

    def posible_tateti_diagonal_primaria(self,tablero):
        x = tablero.primera_fila()
        while x <= tablero.ultima_fila():
            if tablero.ver(x,x) != NADA and tablero.ver(x,x) != self.ficha:
                return False
            x += 1
        return True

    def posible_tateti_diagonal_secundaria(self,tablero):
        f = tablero.primera_fila()
        c = tablero.ultima_columna()        
        while f <= tablero.ultima_fila():
            if tablero.ver(f,c) != NADA and tablero.ver(f,c) != self.ficha:
                return False
            f += 1
            c -= 1
        return True

    def hay_fichas_propias_fila(self,tablero,fila):
        for columna in range(tablero.primera_columna(),tablero.ultima_columna()):
            if tablero.ver(fila,columna) == self.ficha:
                return True
        return False

    def hay_fichas_propias_columna(self,tablero,columna):
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()):
            if tablero.ver(fila,columna) == self.ficha:
                return True
        return False

    def hay_fichas_propias_diagonal_primaria(self,tablero):
        x = tablero.primera_fila()
        while x <= tablero.ultima_fila():
            if tablero.ver(x,x) == self.ficha:
                return True
            x += 1
        return False

    def hay_fichas_propias_diagonal_secundaria(self,tablero):
        f = tablero.primera_fila()
        c = tablero.ultima_columna()        
        while f <= tablero.ultima_fila():
            if tablero.ver(f,c) == self.ficha:
                return True
            f += 1
            c -= 1
        return False

    def posibilidades_diagonal_primaria(self,tablero,posibles_coordenadas):
        x = tablero.primera_fila()
        while x <= tablero.ultima_fila():
            if self.posible_tateti_diagonal_primaria(tablero) and self.hay_fichas_propias_diagonal_primaria(tablero):
                if tablero.ver(x,x) == NADA:
                    if (x,x) not in posibles_coordenadas.keys():
                        posibles_coordenadas[(x,x)] = 1.0
                    else:
                        posibles_coordenadas[(x,x)] += 1.0
            elif self.posible_tateti_diagonal_primaria(tablero):
                if (x,x) not in posibles_coordenadas.keys():
                    posibles_coordenadas[(x,x)] = 0.3
                else:
                    posibles_coordenadas[(x,x)] += 0.3
            x += 1

    def posibilidades_diagonal_secundaria(self,tablero,posibles_coordenadas):
        f = tablero.primera_fila()
        c = tablero.ultima_columna()        
        while f <= tablero.ultima_fila():
            if self.posible_tateti_diagonal_secundaria(tablero) and self.hay_fichas_propias_diagonal_secundaria(tablero):
                if tablero.ver(f,c) == NADA:
                    if (f,c) not in posibles_coordenadas.keys():
                        posibles_coordenadas[(f,c)] = 1.0
                    else:
                        posibles_coordenadas[(f,c)] += 1.0
            elif self.posible_tateti_diagonal_secundaria(tablero):
                if (f,c) not in posibles_coordenadas.keys():
                    posibles_coordenadas[(f,c)] = 0.3
                else:
                    posibles_coordenadas[(f,c)] += 0.3
            f += 1
            c -= 1

    def posibilidades_columnas(self,tablero,posibles_coordenadas):        
        for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
            if self.posible_tateti_columna(tablero,columna) and self.hay_fichas_propias_columna(tablero,columna):
                for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
                    if tablero.ver(fila,columna) == NADA:
                        if (fila,columna) not in posibles_coordenadas.keys():
                            posibles_coordenadas[(fila,columna)] = 1.0
                        else:
                            posibles_coordenadas[(fila,columna)] += 1.0
            elif self.posible_tateti_columna(tablero,columna):
                for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
                    if (fila,columna) not in posibles_coordenadas.keys():
                        posibles_coordenadas[(fila,columna)] = 0.3
                    else:
                        posibles_coordenadas[(fila,columna)] += 0.3
        
    def posibilidades_filas(self,tablero,posibles_coordenadas):        
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            if self.posible_tateti_fila(tablero,fila) and self.hay_fichas_propias_fila(tablero,fila):
                for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                    if tablero.ver(fila,columna) == NADA:
                        if (fila,columna) not in posibles_coordenadas.keys():
                            posibles_coordenadas[(fila,columna)] = 1.0
                        else:
                            posibles_coordenadas[(fila,columna)] += 1.0
            elif self.posible_tateti_fila(tablero,fila):
                for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                    if (fila,columna) not in posibles_coordenadas.keys():
                        posibles_coordenadas[(fila,columna)] = 0.3
                    else:
                        posibles_coordenadas[(fila,columna)] += 0.3

    def elegir_mejor_posibilidad(self,posible_coordenadas):
        mejor_coordenada=(-1,-1)
        posible_coordenadas[mejor_coordenada] = 0
        for coordenada in posible_coordenadas:
            if posible_coordenadas[coordenada] > posible_coordenadas[mejor_coordenada]:
                mejor_coordenada = coordenada
        return Coordenada(mejor_coordenada[0],mejor_coordenada[1])
                

    def posibilidades(self,tablero):
        posibles_coordenadas={}
        self.posibilidades_diagonal_primaria(tablero,posibles_coordenadas)
        self.posibilidades_diagonal_secundaria(tablero,posibles_coordenadas)
        self.posibilidades_filas(tablero,posibles_coordenadas)
        self.posibilidades_columnas(tablero,posibles_coordenadas)

        coor = self.elegir_mejor_posibilidad(posibles_coordenadas)
        return coor

    def primer_lugar_vacio(self,tablero):
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                if tablero.ver(fila,columna) == NADA:
                    return Coordenada(fila,columna)

    def sumar_jugada(self):
        self.jugadas +=1

    def segundo_ataque(self,tablero):
        if self.posible_tateti_columna(tablero,tablero.primera_columna()) and self.posible_tateti_diagonal_secundaria(tablero):
            return Coordenada(tablero.ultima_fila(),tablero.primera_columna())
        elif not self.posible_tateti_columna(tablero,tablero.primera_columna()) or not self.posible_tateti_diagonal_secundaria(tablero):
            return Coordenada(tablero.ultima_fila(),tablero.ultima_columna())
        else:
            return Coordenada(tablero.primera_fila(),tablero.ultima_columna())

    def atacar(self,tablero):
        coor = self.atacar_filas(tablero)
        if coor != False:
            return coor
        coor = self.atacar_columnas(tablero)
        if coor != False:
            return coor
        coor = self.atacar_diagonales(tablero)
        if coor != False:
            return coor
        return False

    def modo_ataque(self,tablero):
        if self.jugadas == 0:
            self.sumar_jugada()
            return Coordenada(tablero.primera_fila(),tablero.primera_columna())
        elif self.jugadas == 1:
            self.sumar_jugada()
            return self.segundo_ataque(tablero)        
        coor = self.atacar(tablero)
        if coor != False:
            return coor
        coor = self.defender(tablero)
        if coor != False:
            return coor
        coor = self.posibilidades(tablero)
        if coor != False:
            return coor
        return self.primer_lugar_vacio(tablero)

    def modo_defensa(self,tablero):
        if self.jugadas == 0:
            if tablero.ver(tablero.ultima_fila()//2,tablero.ultima_columna()//2) == NADA:
                self.sumar_jugada()
                return Coordenada(tablero.ultima_fila()//2,tablero.ultima_columna()//2)
            else:
                self.sumar_jugada()
                return Coordenada(tablero.primera_fila(),tablero.primera_columna())
        coor = self.atacar(tablero)
        if coor != False:
            return coor
        coor = self.defender(tablero)
        if coor != False:
            return coor 
        if self.jugadas == 1:
            self.sumar_jugada()
            if tablero.ver(tablero.primera_fila(),tablero.primera_columna()) != NADA and tablero.ver(tablero.primera_fila()+1,tablero.primera_columna()) == NADA :
                return Coordenada(tablero.primera_fila()+1,tablero.primera_columna())
            elif tablero.ver(tablero.primera_fila(),tablero.primera_columna()) != NADA and tablero.ver(tablero.primera_fila()+1,tablero.primera_columna()) != NADA :
                return Coordenada(tablero.primera_fila(),tablero.primera_columna()+1)  
        coor = self.posibilidades(tablero)
        if coor != False:
            return coor
        return self.primer_lugar_vacio(tablero)

    def jugar(self,tablero):
        if self.jugadas == 0:
            self.primer_jugador = self.es_primer_jugador(tablero)
        if self.primer_jugador:
            return self.modo_ataque(tablero)
        else:
            return self.modo_defensa(tablero)
# -------------------------------------------------------------------------
class Coordenada:
    def __init__(self, fila=0, columna=0):
        self.fila = fila
        self.columna = columna
# -------------------------------------------------------------------------
class Tateti:
    def __init__(self, jug1, jug2):
        
        self.jug1 = jug1
        self.jug2 = jug2
        self.tablero = Tablero()

    def jugarTateti(self):
        
        """os.system("cls")"""
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
            """os.system("cls")"""
            print(str(self.tablero))
            if self.esTateti(jugAux.ficha):
                ganar = True
            else:
                jugAux = self.elOtroJugador(jugAux)
                
        if ganar:
            print("Ganador: " + str(jugAux))
            return jugAux
        else:
            print("Empate!!!!!!!")
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
# -------------------------------------------------------------------------
def main():
    
    jugCompu1 = Computadora_nivel3("Computadora", CIRC)
    jugHumano = Humano("Humano", CRUZ)
    juego = Tateti(jugCompu1, jugHumano)
    juego.jugarTateti()

# -------------------------------------------------------------------------
main()