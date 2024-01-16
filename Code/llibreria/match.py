from slam import *
from queue import Queue
from entitat import entitat
from motorEventsDiscrets import *

class match(slamiii):

    def __init__(self, scheduler, parametres):
        super(match, self).__init__(scheduler, parametres)

        self.parametres = parametres
        llista_atributs = parametres.split(',')

        self.atr = int(llista_atributs[0])
        self.DST1 = int(llista_atributs[1])
        self.DST2 = int(llista_atributs[2])

        self.set_estat(Estat.LLIURE)
        self.cuaEspera = Queue()  # Cua per entitats en espera
        self.entitatsProcesades = 0

    def __repr__(self):
        return "match"

    def tractarEsdeveniment(self, event):
        '''
        Si estic LLIURE i arriba una entitat, comprovo si hi ha alguna entitat en espera amb el mateix valor a l'atribut ATR.
        - Si sí, paso l'entitat actual per DST1 i l'entitat en espera per DST2.
        - Si no, poso l'entitat en espera.
        '''
        if self.get_estat() == Estat.LLIURE:

            if not self.cuaEspera.empty():
                # Hi ha una entitat en espera
                entitatEspera = self.cuaEspera.get()

                # Verificar si tenen el mateix valor en l'atribut ATR
                if event.entitat.get_atribut(self.atr) == entitatEspera.get_atribut(self.atr):
                    self.traspassarEntitat(event.entitat, self.DST1)
                    self.traspassarEntitat(entitatEspera, self.DST2)
                    self.entitatsProcesades += 2
                else:
                    # No coincideixen, per tant posem les entitats en espera
                    self.cuaEspera.put(event.entitat)
                    self.cuaEspera.put(entitatEspera)
            else:
                # No hi ha entitat, posar l'entitat actual en espera
                self.cuaEspera.put(event.entitat)

    def iniciSimulacio(self):
        super(match, self).iniciSimulacio()
        pass

    def fiSimulacio(self):
        super(match, self).fiSimulacio()
        pass

    def acceptaEntitat(self, n):
        self.acceptaEntitat(n)
        pass

    def summary(self):
        return " EST: " + str(self.entitatsProcesades)
