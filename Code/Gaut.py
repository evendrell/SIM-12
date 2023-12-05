from oppregninger import *
import math
from Event import *
from Bil import *


class Gaut:

    def __init__(self,veuretraza):
        # inicialitzar element de simulacio
        self.entitatsSortides=0
        self.state=State.SERVICE
        self.livAvg=0
        self.veuretraza=veuretraza

    def tractarEsdeveniment(self, event):
        if (event.type==EventType.Tranfer):
            self.processTransfer(event)        

    def simulationStart(self):
        self.entitatsSortides=0
        pass

    def processTransfer(self,event):
        # Fer quelcom d'estadistics
        avg=self.livAvg*self.entitatsSortides
        self.entitatsSortides=self.entitatsSortides+1
        event.entitat.gaut(event.tid)
        self.livAvg=(self.livAvg+event.entitat.livstid)/self.entitatsSortides
        if (self.veuretraza==0):
            return
        print(Colors.HEADER,event.tid,' Ga ut bilen fra ',event.fra,' livstid ',event.entitat.livstid,Colors.OKGREEN,' livsAvg ',self.livAvg,Colors.ENDC)
        # Memoritzar temps de vida

        pass
    
    def summary(self):
        print('Entitats sortides del sistema: ',self.entitatsSortides)
        print('Temps mig de vida: ',self.livAvg)

    def __repr__(self):
        return "Ga ut"
    
   