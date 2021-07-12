from coordenada import Coordenada
from jugadores.jugadores import Jugador
import random as R
from ficha import CIRC,CRUZ,NADA

class ComputadoraDificil(Jugador):

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
            return coor
        coor = self.defender_columnas(tablero)
        if coor != False:
            return coor
        coor = self.defender_diagonales(tablero)
        if coor != False:
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
