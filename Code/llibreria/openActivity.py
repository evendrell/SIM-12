from slam import *
from entitat import *
from gate import *

class openActivity(slamiii):

    # conèixer el motor de simulació pot anar molt bé
    def __init__(self, scheduler, parametres):
        super(openActivity, self).__init__(scheduler, parametres)
        # Que faig amb parametres, en aquest cas nop
        self.parametres = parametres
        lista_atributos = parametres.split(',')
        self.GATE = int(lista_atributos[2])
        self.M = int(lista_atributos[3])
        self.estadisticOpenGates = 0
        self.set_estat(Estat.LLIURE)

    def __repr__(self):
        return "openActivity"

    def tractarEsdeveniment(self, event):
        if event.tipus == TipusEvent.ObrirPortaEnTTics:
            self.obraPortaEnTTicsGate(event)

    def iniciSimulacio(self):
        super(openActivity, self).iniciSimulacio()
        self.estadisticOpenGates = 0
        self.GATE = self.scheduler.donamActivitat(int(self.GATE))
        self.set_estat(Estat.LLIURE)
        pass

    def fiSimulacio(self):
        super(openActivity, self).fiSimulacio()
        pass

    def obraPortaEnTTicsGate(self, event):
        # Llamamos a la función obraPortaEnTTics del gate asociado
        self.estadisticOpenGates += 1
        self.GATE.obraPortaEnTTics(event)

    def acceptaEntitat(self, n):
        # aquí estic suposant que n'ho accepto res
        return 0

    def summary(self):
        # Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        return " EST: Num vegades que he obert la porta: " + str(self.estadisticOpenGates)