from coordenada import Coordenada
from jugadores.jugadores import Jugador
import random as R
from ficha import CIRC,CRUZ,NADA


LISTA_COORDENADAS = {'columnas':[[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)]],
'filas':[[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]],'diagonales':[[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]}

class ComputadoraDificil(Jugador):

    def __init__(self, nombre, ficha, primer_jugador=False, jugadas=0):
        super().__init__(nombre=nombre, ficha=ficha)
        self.primer_jugador = primer_jugador
        self.jugadas = jugadas 
        self.setFichaContrario()

    def setFichaContrario(self):
        if self.ficha == CRUZ:
            self.ficha_contrario = CIRC
        else:
            self.ficha_contrario = CRUZ

    def hayFichasPropiasRango(self,tablero,coordenadas):
        #Recorre una fila y devuelte True si encuntra alguna ficha nuestra
        res = False
        for coordenda in coordenadas:
            if tablero.ver(coordenda[0],coordenda[1]) == self.ficha:
                res = True
        return res

    def hayFichasPropiasRangos(self,tablero,lts_coordenadas):
        #Recorre una fila y devuelte True si encuntra alguna ficha nuestra
        res = False
        for coordenadas in lts_coordenadas:
            if self.hayFichasPropiasRango(tablero,coordenadas):
                res = True
                break
        return res

    def primer_lugar_vacio(self,tablero):
        #Recorre el tablero y devuelve el primer lugar vacio
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                if tablero.ver(fila,columna) == NADA:
                    return Coordenada(fila,columna)

    def sumarJugada(self):
        #Suma 1 a las jugadas hechas
        self.jugadas +=1  
    
    def elegir_mejor_posibilidad(self,posible_coordenadas):
        # Empieza con una coordenada absurda para comparar
        mejor_coordenada=(-1,-1)
        posible_coordenadas[mejor_coordenada] = 0
        for coordenada in posible_coordenadas:
            # Recorre todas las coordenadas y compara cual tiene mas puntaje
            if posible_coordenadas[coordenada] > posible_coordenadas[mejor_coordenada]:
                mejor_coordenada = coordenada
        # Devuelve la coordeanada de mayor puntaje
        return Coordenada(mejor_coordenada[0],mejor_coordenada[1])
    
    def chequearRangoTapado(self,tablero,lst_coordenadas):
        #Dentro de una fila recorre las columnas
        res = False
        for coordenada in lst_coordenadas:
            # Si encuentra una ficha del oponente devuelve False
            # ya que en esa fila no hay posibilidades de hacer TATETI
            if tablero.ver(coordenada[0],coordenada[1]) == self.ficha_contrario:
                res = True
                break
        # Si no encuentra una ficha del oponente devuelve True
        # ya que en esa fila hay posibilidades de hacer TATETI
        return res

    def chequearRangosTapados(self,tablero):
        #Dentro de una fila recorre las columnas
        res = False
        for llaves in LISTA_COORDENADAS.keys():
            # Si encuentra una ficha del oponente devuelve False
            # ya que en esa fila no hay posibilidades de hacer TATETI
            if self.chequearRangoTapado(tablero,LISTA_COORDENADAS[llaves]):
                res = True
                break
        # Si no encuentra una ficha del oponente devuelve True
        # ya que en esa fila hay posibilidades de hacer TATETI
        return res

    def sumarPuntajeCoordenada(self,coordenada,posibles_coordenadas,pts):
        if (coordenada[0],coordenada[1]) not in posibles_coordenadas.keys():
            posibles_coordenadas[(coordenada[0],coordenada[1])] = pts
        #En caso que ya este en el diccionario se le suma 1 punto
        else:
            posibles_coordenadas[(coordenada[0],coordenada[1])] += pts

    def posibilidadesRango(self,tablero,posibles_coordenadas,coordenadas):
        for coordenada in coordenadas:
            if tablero.ver(coordenada[0],coordenada[1]) == NADA:
                #En caso que no este en el diccionario se crea una llave con esa coordenada y se le suma 1 punto
                self.sumarPuntajeCoordenada(coordenada,posibles_coordenadas,1.0)
            elif self.chequearRangoTapado(tablero,coordenadas) == True:
                #En caso que no este en el diccionario se crea una llave con esa coordenada y se le suma 0.3 puntos
                self.sumarPuntajeCoordenada(coordenada,posibles_coordenadas,1.0)


    def posibilidadesRangos(self,tablero,posibles_coordenadas,lst_coordenadas):
        #Recorre la diagonal
        for coordenadas in lst_coordenadas:
            if self.chequearRangoTapado(tablero,coordenadas) == False and self.hayFichasPropiasRango(tablero,coordenadas) == True:
                self.posibilidadesRango(tablero,posibles_coordenadas,coordenadas)                

    def posibilidades(self,tablero):
        # Crea un diccionario vacio para guardar las posibles coordenadas para hacer TATETI
        posibles_coordenadas={}
        for llaves in LISTA_COORDENADAS:
            self.posibilidadesRango(tablero,posibles_coordenadas,LISTA_COORDENADAS[llaves])
        coor = self.elegir_mejor_posibilidad(posibles_coordenadas)
        return coor

    def rematar_tateti(self,tablero,lst_coordenadas,ficha):
        fichas = 0
        lugar_vacio = 0
        #Dentro de una columna recorre las filas
        for coordenada in lst_coordenadas:
            # Si en la posicion encuentra una ficha del jugador suma 1 a fichas
            if tablero.ver(coordenada[0],coordenada[1]) == ficha:
                fichas += 1
            # Si en la posicion encuentra un lugar vacio suma 1 lugar_vacio
            # y guarda las coordenadas de ese lugar vacio
            elif tablero.ver(coordenada[0],coordenada[1]) == NADA:
                lugar_vacio +=1
                coordenada_vacia = Coordenada(coordenada[0],coordenada[1]) 
        # Si en esa columna el jugador tiene 2 fichas y hay 1 lugar vacio
        # devuelve las coordenadas del lugar vacio para que el jugador haga TATETI
        if fichas == 2 and lugar_vacio == 1:
            return coordenada_vacia
        # Si no hay posibilidades de hacer TATETI devuelve None                                                            
        return None

    def rematar(self,tablero,lst_coordenadas,ficha):
        for coordenadas in lst_coordenadas:
            coordenada = self.rematar_tateti(tablero,coordenadas,ficha)
            if coordenada:
                break
        return coordenada

    def chequear_remate(self,tablero,ficha):
        for lst_coordenadas in LISTA_COORDENADAS.keys():
            coordenada = self.rematar(tablero,LISTA_COORDENADAS[lst_coordenadas],ficha)
            if coordenada:
                    break
        return coordenada

    def defender(self,tablero):
        return self.chequear_remate(tablero,self.ficha_contrario)
    
    def atacar(self,tablero):
        return self.chequear_remate(tablero,self.ficha)

    def segundo_ataque(self,tablero):
        # Revisa si es posible hacer tateti en la primer columna [(0,0),(1,0),(2,0)]
        # y en la diagonal secundaria [(1,3),(2,2),(3,1)] si las dos condiciones se dan,
        # el mejor lugar para poner la ficha es (3,1)
        coor = None
        if self.chequearRangosTapado(tablero,[LISTA_COORDENADAS['columnas'][0],LISTA_COORDENADAS['columnas'][0]]) == False and self.hayFichasPropiasRango(tablero,[LISTA_COORDENADAS['columnas'][0],LISTA_COORDENADAS['diagonales'][1]]) == True:
            coor = Coordenada(tablero.ultima_fila(),tablero.primera_columna())
        # Revisa si no es posible hacer tateti en la primer columna [(1,1),(2,1),(3,1)]
        # o no es posible en la diagonal secundaria [(1,3),(2,2),(3,1)] si alguna de las
        # condiciones no se cumple, el mejor lugar para poner la ficha es (3,3)
        elif self.chequearRangoTapado(tablero,LISTA_COORDENADAS['columnas'][0]) or self.chequearRangoTapado(tablero,LISTA_COORDENADAS['diagonales'][1]):
            coor = Coordenada(tablero.ultima_fila(),tablero.ultima_columna())
        # Y como ultima opcion pone la ficha en (1,3)
        else:
            coor = Coordenada(tablero.primera_fila(),tablero.ultima_columna())
        return coor

    def modo_defensa(self,tablero):
        #Primer movimiento
        if self.jugadas == 0:
            #Si en la posicion del medio (2,2) no hay nada coloca una ficha ahi
            if tablero.ver(tablero.ultima_fila()//2,tablero.ultima_columna()//2) == NADA:
                self.sumarJugada()
                return Coordenada(tablero.ultima_fila()//2,tablero.ultima_columna()//2)
            #En caso que el centro este ocupado, coloca la ficha en el lugar (1,1)
            else:
                self.sumarJugada()
                return Coordenada(tablero.primera_fila(),tablero.primera_columna())
        # Se fija si puede rematar el partido 
        coor = self.atacar(tablero)
        if coor != False:
            # En caso positivo realiza el movimento
            return coor
        # Sino pudo rematar, revisa que no este por perder
        coor = self.defender(tablero)
        if coor != False:
            # En caso positivo realiza el movimento
            return coor 
        # Si es su segundo movimento
        if self.jugadas == 1:
            self.sumarJugada()
            # Si la ubicacion (1,1) no esta vacia y (2,1) si esta vacia devuelve esa coordenada para poner ficha
            if tablero.ver(tablero.primera_fila(),tablero.primera_columna()) != NADA and tablero.ver(tablero.primera_fila()+1,tablero.primera_columna()) == NADA :
                return Coordenada(tablero.primera_fila()+1,tablero.primera_columna())
            # Si la ubicacion (1,1) no esta vacia y (2,1) tampoco esta vacia devuelve (1,2) para poner ficha
            elif tablero.ver(tablero.primera_fila(),tablero.primera_columna()) != NADA and tablero.ver(tablero.primera_fila()+1,tablero.primera_columna()) != NADA :
                return Coordenada(tablero.primera_fila(),tablero.primera_columna()+1)  
        # Y si no busca el lugar mas conveniente para poner una ficha
        coor = self.posibilidades(tablero)
        if coor != False:
            return coor
        # Y como ultima opcion devuelve el primer lugar vacio que encuentre
        return self.primer_lugar_vacio(tablero)

    def modo_ataque(self,tablero):
        #Si es el primer movimiento pone ficha en 1,1
        if self.jugadas == 0:
            self.sumarJugada()
            return Coordenada(tablero.primera_fila(),tablero.primera_columna())
        #Si es su segundo movimiento activa el segundo ataque
        elif self.jugadas == 1:
            self.sumarJugada()
            return self.segundo_ataque(tablero)
        # Se fija si puede rematar el partido   
        coor = self.atacar(tablero)
        if coor != False:
            # En caso positivo realiza el movimento
            return coor
        # Sino pudo rematar, revisa que no este por perder
        coor = self.defender(tablero)
        if coor != False:
            # En caso positivo realiza el movimento
            return coor
        # Y si no busca el lugar mas conveniente para poner una ficha
        coor = self.posibilidades(tablero)
        if coor != False:
            # En caso positivo realiza el movimento
            return coor
        # Y como ultima opcion devuelve el primer lugar vacio que encuentre
        return self.primer_lugar_vacio(tablero)

    def es_primer_jugador(self,tablero):
        # Recorre todo el tablero, si encuentra una ficha devuelve False, en caso de que este vacio devuelve True
        for f in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            for c in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                if tablero.ver(f,c) != NADA:
                    return False
        return True

    def jugar(self,tablero):
        # Revisa si el tablero esta vacio o si ya hay una ficha
        if self.jugadas == 0:
            self.primer_jugador = self.es_primer_jugador(tablero)        
        if self.primer_jugador:
            # Si le toca jugar primero, activa el modo ataque
            return self.modo_ataque(tablero)
        else:
            # Si le toca jugar segundo, activa el modo defensa
            return self.modo_defensa(tablero)
