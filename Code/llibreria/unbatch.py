from slam import *
from entitat import *

class unbatch(slamiii):
    def __init__(self, scheduler, parametres):
        super(unbatch, self).__init__(scheduler, parametres)
        self.parametres = parametres
        llista_atributs = parametres.split(',')
        self.m = int(llista_atributs[1])
        self.TO1 = int(llista_atributs[2])
        self.TO2 = int(llista_atributs[3])

        self.estadisticRebudes = 0
        self.estadisticCreades = 0

        self.set_estat(Estat.LLIURE)

    def __repr__(self):
        return "unbatch"
    
    def tractarEsdeveniment(self, event):
        if self.get_estat() == Estat.LLIURE:
            self.estadisticRebudes += 1
            self.set_estat(Estat.BATCHING)
            llista_entitats = [event*self.m]
            self.estadisticCreades += self.m
            for n in range(self.m):
                if n % 2 == 0:
                    self.traspassarEntitat(llista_entitats[n], self.TO1)
                else:
                    self.traspassarEntitat(llista_entitats[n], self.TO2)
            self.set_estat(Estat.LLIURE)

    def iniciSimulacio(self):
        super(unbatch, self).iniciSimulacio()
        self.TO1 = self.scheduler.donamActivitat(self.T01+1)
        self.TO2 = self.scheduler.donamActivitat(self.T02+1)
    
    def fiSimulacio(self):
        super(unbatch, self).fiSimulacio()

    def acceptaEntitat(self, _):
        return self.get_estat() == Estat.LLIURE

    def summary(self):
        return " EST: "+str(self.estadisticRebudes)+' '+str(self.estadisticCreades)
