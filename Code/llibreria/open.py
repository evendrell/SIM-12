from slam import *
from entitat import *
from gate import *


class open(slamiii):

    # conèixer el motor de simulació pot anar molt bé
    def __init__(self, scheduler, parametres):
        super(open, self).__init__(scheduler, parametres)
        # Que faig amb parametres, en aquest cas nop
        self.parametres = parametres
        lista_atributos = parametres.split(',')
        self.GATE = int(lista_atributos[0])
        self.M = int(lista_atributos[1])
        self.set_estat(Estat.LLIURE)

    def __repr__(self):
        return "open"

    def tractarEsdeveniment(self, event):
        pass

    def iniciSimulacio(self):
        # Jo no he de fer res
        pass

    def fiSimulacio(self):
        # Aquí tampoc faig res
        pass

    def acceptaEntitat(self, n):
        # aquí estic suposant que n'ho accepto res, us convenç?
        return 0

    def summary(self):
        # Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        return " EST: 0,0"


