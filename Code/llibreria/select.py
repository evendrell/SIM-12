from slam import *

class select(slamiii):


   



    #Código chorizeado
    def iniciSimulacio(self):
        super(select, self).iniciSimulacio()
        self.entren=0
        self.set_estat(Estat.LLIURE)
        print('Soc nop i he rebut un iniciSimulacio')
        #Jo no he de fer res
        pass
    
    def fiSimulacio(self):
        #Aquí tampoc faig res
        pass
 
    def acceptaEntitat(self, n):
        #aquí estic suposant que ho accepto tot, us convenç?
        return n
    
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        return " EST: "+str(self.entren)+' '+str(self._surten)