from slam import *

class blockActivity(slamiii):
    
     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(blockActivity, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.parametres=parametres
        
    def __repr__(self):
        return "block"
        
    def tractarEsdeveniment(self, event):
        #Soc nop no importa el meu estat ni el meu event, simplement no faig res
        #un altre opcio per a blockejar seria no traspassar l'entitat
        pass      

    def iniciSimulacio(self):
        self.estat(Estat.BLOQUEJAT)
        print('Soc block i he rebut un iniciSimulacio')
        #Jo no he de fer res
        pass
    
    def fiSimulacio(self):
        #Aquí tampoc faig res
        pass
 
    def acceptaEntitat(self, n):
        #aquí estic suposant que n'ho accepto res, us convenç?
        return 0
    
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        print('Doncs ja estarem')
        
        
