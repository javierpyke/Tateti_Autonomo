class Ficha:
    def __init__(self, caracter):
        self.caracter = caracter

    def __str__(self):
        return '['+self.caracter+']'

    def __eq__(self,ficha):
        if self.caracter == ficha.caracter:
            return True
        else:
            return False
 
CRUZ = Ficha('X')
CIRC = Ficha('O')
NADA = Ficha(' ')