from slam import *
from entitat import entitat
import random

class activity(slamiii):
    def __init__(self,scheduler,parametres):
        super(activity, self).__init__(scheduler,parametres)
        
        self.parametres=parametres
        parameters_list = parametres.split(',')
        self.N = int(parameters_list[2])
        self.MIN = int(parameters_list[3])
        self.MAX = int(parameters_list[4])

        self.entitats = 0

        self.set_estat(Estat.LLIURE)

        
    def __repr__(self):
        return "activity "+str(self.id())
        
    def tractarEsdeveniment(self, event):
        if self.estat == Estat.LLIURE:
            self.set_estat(Estat.SERVEI)

        # procesem les entitats
        self.entitats = self.entitats - 1

        if (self.entitats == 0):
            self.set_estat(Estat.LLIURE)

    def iniciSimulacio(self):
        super(activity, self).iniciSimulacio()
        self.set_estat(Estat.LLIURE)
        
        pass
    
    def fiSimulacio(self):
        self.set_estat(Estat.LLIURE)
        pass
 
    def acceptaEntitat(self, n):
        self.entitats = n
        self.T = random.uniform(self.MIN, self.MAX)

        self.set_estat(Estat.SERVEI)

        #return n
    
    def summary(self):
        return ""
        
        
