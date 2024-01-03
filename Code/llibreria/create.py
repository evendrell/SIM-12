import numpy

from entitat import *
from slam import *


class create(slamiii):

    # conèixer el motor de simulació pot anar molt bé
    def __init__(self, scheduler, parametres):
        super(create, self).__init__(scheduler, parametres)
        # Que faig amb parametres, en aquest cas nop
        self.parametres = parametres
        llista_atributs = parametres.split(',')
        # Esther t'he corregit l'accés als paràmetres dons els dos primers són l'identificador de l'activitat i el tipus activitat
        self.MAX = int(llista_atributs[2])
        self.T = llista_atributs[3]
        self.M = int(llista_atributs[4])
        self.estadisticEntitatsCreades = 0
        self.estadisticEsdevenimentsProcesats = 0
        self.numeroEntitatsCreades = 0
        self.novaEntitat = None
        self.set_estat(Estat.LLIURE)

    def __repr__(self):
        return "create"

    # FUNCIO PER CREAR NOVES ENTITATS
    def creaEntitat(self):
        self.traspassarEntitat(entitat(), self._successor)

    def tractarEsdeveniment(self, event):
        # Soc nop no importa el meu estat ni el meu event, simplement no faig res
        # un altre opcio per a blockejar seria no traspassar l'entitat
        if event.tipus == TipusEvent.CreaMentitats:
            if self.numeroEntitatsCreades < self.MAX:
                for y in range(self.M):
                    self.numeroEntitatsCreades += 1
                    self.estadisticEntitatsCreades += 1
                    self.creaEntitat()
                self.estadisticEsdevenimentsProcesats += 1
                self.scheduler.afegirEsdeveniment(
                    esdeveniment(self, self.programacioProperaArribada(), TipusEvent.CreaMentitats, None))

    def iniciSimulacio(self):
        super(create, self).iniciSimulacio()
        self.scheduler.afegirEsdeveniment(
            esdeveniment(self, self.programacioProperaArribada(), TipusEvent.CreaMentitats, None))
        self.set_estat(Estat.SERVEI)

    def programacioProperaArribada(self):
        return self.scheduler.temps() + numpy.exp(self.T)

    def fiSimulacio(self):
        # Aquí tampoc faig res
        pass

    def acceptaEntitat(self, n):
        # aquí estic suposant que n'ho accepto res, us convenç?
        return 0

    def summary(self):
        # Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        return " EST: " + str(self.estadisticEsdevenimentsProcesats) + ' ' + str(self.estadisticEntitatsCreades)
