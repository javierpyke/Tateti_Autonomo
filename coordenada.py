class Coordenada:
    def __init__(self, fila=0, columna=0):
        self.fila = fila
        self.columna = columna

    def __str__(self):
        return '({},{})'.format(self.fila,self.columna)

