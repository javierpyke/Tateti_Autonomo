import random as R

class Jugador(object):
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def __str__(self):
        return self.nombre + " ==> "+str(self.ficha)

# -------------------------------------------------------------------------


