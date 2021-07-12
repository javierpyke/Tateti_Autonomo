from ficha import NADA
class Tablero:
    
    def __init__(self, filas=3, columnas=3):
        self.cf = filas
        self.cc = columnas
        self.mat = []
        #Llena el tablero con fichas vacias
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
        cadena = "  1  2  3\n"
        for f in range(self.cf):
            cadena += str(f+1)
            for c in range(self.cc):
                cadena += str(self.mat[f][c])
            cadena += "\n"
        return cadena

    def poner(self, f, c, ficha):
        self.mat[f][c] = ficha

    def ver(self, f, c):
        return self.mat[f][c]

    def existe(self, ficha):
        #Recorre toda la matriz buscando si hay alguna ficha dada
        for f in range(self.cf):
            for c in range(self.cc):
                if ficha == self.mat[f][c]:
                    return True
        return False

    def filaIgual(self, fila, ficha):
        #Recorre una fila
        for c in range(self.cc):
            #Si encuentra una ficha diferente a la dada devuelve False
            if ficha != self.mat[fila][c]:
                return False
        #En caso que sean todas las fichas iguales a las dadas devuelve True
        return True

    def columnaIgual(self, columna, ficha):
        #Recorre una columna
        for f in range(self.cf):
            #Si encuentra una ficha diferente a la dada devuelve False
            if ficha != self.mat[f][columna]:
                return False
        #En caso que sean todas las fichas iguales a las dadas devuelve True
        return True

    def digonalIgual(self, ficha):
        for x in range(self.cf):
            #Si encuentra una ficha diferente a la dada devuelve False
            if self.mat[x][x] != ficha:
                return False
        #En caso que sean todas las fichas iguales a las dadas devuelve True
        return True

    def digonalSecIgual(self, ficha):
        f = 0
        c = self.cc-1
        while f < self.cf:
            #Si encuentra una ficha diferente a la dada devuelve False
            if self.mat[f][c] != ficha:
                return False
            f += 1
            c -= 1
        #En caso que sean todas las fichas iguales a las dadas devuelve True
        return True