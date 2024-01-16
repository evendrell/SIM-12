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
        self.GATE = (lista_atributos[2])
        self.M = int(lista_atributos[3])
        self.estadisticOpenGates = 0
        self.set_estat(Estat.LLIURE)

    def __repr__(self):
        return "open"

    def tractarEsdeveniment(self, event):
        if event.tipus == TipusEvent.ObrirPortaEnTTics:
            self.obraPortaEnTTics(event)

    def iniciSimulacio(self):
        super(open, self).iniciSimulacio()
        self.estadisticOpenGates = 0
        self.set_estat(Estat.LLIURE)
        pass

    def fiSimulacio(self):
        super(open,self).fiSimulacio()
        pass

    def obraPortaEnTTics(self, event):
        # Llamamos a la función obraPortaEnTTics del gate asociado
        self.estadisticOpenGates += 1
        self.GATE.obraPortaEnTTics(event)

    def acceptaEntitat(self, n):
        # aquí estic suposant que n'ho accepto res
        return 0

    def summary(self):
        # Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        return "EST:"+str(self.estadisticOpenGates)
