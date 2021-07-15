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


    def posible_tateti_columna(self,tablero,columna):
        #Dentro de una columna recorre las filas
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            # Si encuentra una ficha del oponente devuelve False
            # ya que en esa columna no hay posibilidades de hacer TATETI
            if tablero.ver(fila,columna) != NADA and tablero.ver(fila,columna) != self.ficha:
                return False
        # Si no encuentra una ficha del oponente devuelve True
        # ya que en esa columna hay posibilidades de hacer TATETI
        return True

    def posible_tateti_fila(self,tablero,fila):
        #Dentro de una columna recorre las filas
        for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
            # Si encuentra una ficha del oponente devuelve False
            # ya que en esa columna no hay posibilidades de hacer TATETI
            if tablero.ver(fila,columna) != NADA and tablero.ver(fila,columna) != self.ficha:
                return False
        # Si no encuentra una ficha del oponente devuelve True
        # ya que en esa columna hay posibilidades de hacer TATETI
        return True

    def posible_tateti_diagonal_primaria(self,tablero):
        # Recorre la diagonal primaria 
        x = tablero.primera_fila()
        while x <= tablero.ultima_fila():
            # Si encuentra una ficha del oponente devuelve False
            # ya que en esa columna no hay posibilidades de hacer TATETI
            if tablero.ver(x,x) != NADA and tablero.ver(x,x) != self.ficha:
                return False
            x += 1
        # Si no encuentra una ficha del oponente devuelve True
        # ya que en esa columna hay posibilidades de hacer TATETI
        return True

    def posible_tateti_diagonal_secundaria(self,tablero):
        # Recorre la diagonal secundaria 
        f = tablero.primera_fila()
        c = tablero.ultima_columna()        
        while f <= tablero.ultima_fila():
            # Si encuentra una ficha del oponente devuelve False
            # ya que en esa columna no hay posibilidades de hacer TATETI
            if tablero.ver(f,c) != NADA and tablero.ver(f,c) != self.ficha:
                return False
            f += 1
            c -= 1
        # Si no encuentra una ficha del oponente devuelve True
        # ya que en esa columna hay posibilidades de hacer TATETI
        return True

    def hay_fichas_propias_fila(self,tablero,fila):
        #Recorre una fila y devuelte True si encuntra alguna ficha nuestra
        for columna in range(tablero.primera_columna(),tablero.ultima_columna()):
            if tablero.ver(fila,columna) == self.ficha:
                return True
        return False

    def hay_fichas_propias_columna(self,tablero,columna):
        #Recorre una columna y devuelte True si encuntra alguna ficha nuestra
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()):
            if tablero.ver(fila,columna) == self.ficha:
                return True
        return False

    def hay_fichas_propias_diagonal_primaria(self,tablero):
        #Recorre la diagonal principal y devuelte True si encuntra alguna ficha nuestra
        x = tablero.primera_fila()
        while x <= tablero.ultima_fila():
            if tablero.ver(x,x) == self.ficha:
                return True
            x += 1
        return False

    def hay_fichas_propias_diagonal_secundaria(self,tablero):
        #Recorre la diagonal secundaria y devuelte True si encuntra alguna ficha nuestra
        f = tablero.primera_fila()
        c = tablero.ultima_columna()        
        while f <= tablero.ultima_fila():
            if tablero.ver(f,c) == self.ficha:
                return True
            f += 1
            c -= 1
        return False

    def primer_lugar_vacio(self,tablero):
        #Recorre el tablero y devuelve el primer lugar vacio
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                if tablero.ver(fila,columna) == NADA:
                    return Coordenada(fila,columna)

    def sumar_jugada(self):
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
    
    def posibilidades_columnas(self,tablero,posibles_coordenadas):        
        # Recorre las columnas
        for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
            # Si en una columna es posible hacer TATETI en un futuro y hay fichas propias
            if self.posible_tateti_columna(tablero,columna) and self.hay_fichas_propias_columna(tablero,columna):
                #Recorre las filas
                for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
                    # Si el lugar esta vacio 
                    if tablero.ver(fila,columna) == NADA:
                        # Suma un punto a la cooredenada
                        if (fila,columna) not in posibles_coordenadas.keys():
                            posibles_coordenadas[(fila,columna)] = 1.0
                        else:
                            posibles_coordenadas[(fila,columna)] += 1.0
            # En caso de que no haya una ficha propia en la columna pero haya posisibilidad de 
            # hacer TATETI en un futuro se le suma 0.3 puntos a la coordenada
            elif self.posible_tateti_columna(tablero,columna):
                #Recorre las filas
                for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
                    # Se le suma 0.3 puntos a la coordenada
                    if (fila,columna) not in posibles_coordenadas.keys():
                        posibles_coordenadas[(fila,columna)] = 0.3
                    else:
                        posibles_coordenadas[(fila,columna)] += 0.3
    
    def posibilidades_filas(self,tablero,posibles_coordenadas):
        # Recorre las filas      
        for fila in range(tablero.primera_fila(),tablero.ultima_fila()+1):
            # Si en una fila es posible hacer TATETI en un futuro y hay fichas propias
            if self.posible_tateti_fila(tablero,fila) and self.hay_fichas_propias_fila(tablero,fila):
                #Recorre las columnas
                for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                    # Si el lugar esta vacio 
                    if tablero.ver(fila,columna) == NADA:
                        # Suma un punto a la cooredenada
                        if (fila,columna) not in posibles_coordenadas.keys():
                            posibles_coordenadas[(fila,columna)] = 1.0
                        else:
                            posibles_coordenadas[(fila,columna)] += 1.0
            # En caso de que no haya una ficha propia en la fila pero haya posisibilidad de 
            # hacer TATETI en un futuro se le suma 0.3 puntos a la coordenada
            elif self.posible_tateti_fila(tablero,fila):
                #Recorre las columnas
                for columna in range(tablero.primera_columna(),tablero.ultima_columna()+1):
                    # Si hay posibilidad de hacer TATETI en un futuro se le suma 0.3 puntos
                    if (fila,columna) not in posibles_coordenadas.keys():
                        posibles_coordenadas[(fila,columna)] = 0.3
                    else:
                        posibles_coordenadas[(fila,columna)] += 0.3

    def posibilidades_diagonal_secundaria(self,tablero,posibles_coordenadas):
        #Recorre la diagonal
        f = tablero.primera_fila()
        c = tablero.ultima_columna()        
        while f <= tablero.ultima_fila():
            #Si en la diagonal hay posibilidad de hacer TATETI en un futuro y ya hay fichas nuestras
            if self.posible_tateti_diagonal_secundaria(tablero) and self.hay_fichas_propias_diagonal_secundaria(tablero):
                #Y la ubicacion esta vacia
                if tablero.ver(f,c) == NADA:
                    #En caso que no este en el diccionario se crea una llave con esa coordenada y se le suma 1 punto
                    if (f,c) not in posibles_coordenadas.keys():
                        posibles_coordenadas[(f,c)] = 1.0
                    #En caso que ya este en el diccionario se le suma 1 punto
                    else:
                        posibles_coordenadas[(f,c)] += 1.0
            # Si hay posibilidad de hacer TATETI en un futuro pero no tenemos ninguna ficha solo se sumaran 0.3 puntos
            elif self.posible_tateti_diagonal_secundaria(tablero):
                #En caso que no este en el diccionario se crea una llave con esa coordenada y se le suma 0.3 puntos
                if (f,c) not in posibles_coordenadas.keys():
                    posibles_coordenadas[(f,c)] = 0.3
                #En caso que ya este en el diccionario se le suma 0.3 puntos
                else:
                    posibles_coordenadas[(f,c)] += 0.3
            f += 1
            c -= 1

    def posibilidades_diagonal_primaria(self,tablero,posibles_coordenadas):
        #Recorre la diagonal
        x = tablero.primera_fila()
        while x <= tablero.ultima_fila():
            #Si en la diagonal hay posibilidad de hacer TATETI en un futuro y ya hay fichas nuestras
            if self.posible_tateti_diagonal_primaria(tablero) and self.hay_fichas_propias_diagonal_primaria(tablero):
                #Y la ubicacion esta vacia
                if tablero.ver(x,x) == NADA:
                    #En caso que no este en el diccionario se crea una llave con esa coordenada y se le suma 1 punto
                    if (x,x) not in posibles_coordenadas.keys():
                        posibles_coordenadas[(x,x)] = 1.0
                    #En caso que ya este en el diccionario se le suma 1 punto
                    else:
                        posibles_coordenadas[(x,x)] += 1.0
            # Si hay posibilidad de hacer TATETI en un futuro pero no tenemos ninguna ficha solo se sumaran 0.3 puntos
            elif self.posible_tateti_diagonal_primaria(tablero):
                #En caso que no este en el diccionario se crea una llave con esa coordenada y se le suma 0.3 puntos
                if (x,x) not in posibles_coordenadas.keys():
                    posibles_coordenadas[(x,x)] = 0.3
                #En caso que ya este en el diccionario se le suma 0.3 puntos
                else:
                    posibles_coordenadas[(x,x)] += 0.3
            x += 1

    def posibilidades(self,tablero):
        # Crea un diccionario vacio para guardar las posibles coordenadas para hacer TATETI
        posibles_coordenadas={}
        # Revisa las coordenadas de la diagonal primaria [(1,1),(2,2),(3,3)]
        self.posibilidades_diagonal_primaria(tablero,posibles_coordenadas)
        # Revisa las coordenadas de la diagonal primaria [(3,1),(2,2),(1,3)]
        self.posibilidades_diagonal_secundaria(tablero,posibles_coordenadas)
        #Revisa en las filas las posibilidades
        self.posibilidades_filas(tablero,posibles_coordenadas)
        #Revisa en las columnas las posibilidades
        self.posibilidades_columnas(tablero,posibles_coordenadas)
        # Elige cual es la coordenada como mayor puntaje para poner ficha
        coor = self.elegir_mejor_posibilidad(posibles_coordenadas)
        return coor

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









    def rematar_tateti(self,tablero,lst_coordenadas,ficha):
        fichas = 0
        lugar_vacio = 0
        f = tablero.primera_fila()
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
            f += 1
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
        # Revisa si es posible hacer tateti en la primer columna [(1,1),(2,1),(3,1)]
        # y en la diagonal secundaria [(1,3),(2,2),(3,1)] si las dos condiciones se dan,
        # el mejor lugar para poner la ficha es (3,1)
        if self.posible_tateti_columna(tablero,tablero.primera_columna()) and self.posible_tateti_diagonal_secundaria(tablero):
            return Coordenada(tablero.ultima_fila(),tablero.primera_columna())
        # Revisa si no es posible hacer tateti en la primer columna [(1,1),(2,1),(3,1)]
        # o no es posible en la diagonal secundaria [(1,3),(2,2),(3,1)] si alguna de las
        # condiciones no se cumple, el mejor lugar para poner la ficha es (3,3)
        elif not self.posible_tateti_columna(tablero,tablero.primera_columna()) or not self.posible_tateti_diagonal_secundaria(tablero):
            return Coordenada(tablero.ultima_fila(),tablero.ultima_columna())
        # Y como ultima opcion pone la ficha en (1,3)
        else:
            return Coordenada(tablero.primera_fila(),tablero.ultima_columna())

    def modo_defensa(self,tablero):
        #Primer movimiento
        if self.jugadas == 0:
            #Si en la posicion del medio (2,2) no hay nada coloca una ficha ahi
            if tablero.ver(tablero.ultima_fila()//2,tablero.ultima_columna()//2) == NADA:
                self.sumar_jugada()
                return Coordenada(tablero.ultima_fila()//2,tablero.ultima_columna()//2)
            #En caso que el centro este ocupado, coloca la ficha en el lugar (1,1)
            else:
                self.sumar_jugada()
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
            self.sumar_jugada()
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
            self.sumar_jugada()
            return Coordenada(tablero.primera_fila(),tablero.primera_columna())
        #Si es su segundo movimiento activa el segundo ataque
        elif self.jugadas == 1:
            self.sumar_jugada()
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
