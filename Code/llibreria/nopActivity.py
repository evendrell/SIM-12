from slam import *

class nopActivity(slamiii):
    entren=0
     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(nopActivity, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.parametres=parametres
        
    def __repr__(self):
        return "nop "+str(self.id())
        
    def tractarEsdeveniment(self, event):
        #Soc nop no importa el meu estat ni el meu event, simplement deixo passar l'entitat cap endavant
        #No està implementada la transferència hauria de ser un esdeveniment amb el temps actual i màxima prioritat
        self.entren=self.entren+1
        self.traspassarEntitat(event.entitat,self._successor)
        pass      

    def iniciSimulacio(self):
        super(nopActivity, self).iniciSimulacio()
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
        
        
