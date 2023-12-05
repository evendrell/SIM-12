from slam import *

class nopActivity(slamiii):
    
     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(nopActivity, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.parametres=parametres
        
    def __repr__(self):
        return "nop"
        
    def tractarEsdeveniment(self, event):
        #Soc nop no importa el meu estat ni el meu event, simplement no faig res
        pass      

    def iniciSimulacio(self):
        print('Soc nop i he rebut un iniciSimulacio')
        #Jo no he de fer res
        pass
    
    def fiSimulacio(self):
        print('Soc nop i he rebut un fiSimulacio')
        #Aquí tampoc faig res
        pass
 
    def acceptaEntitat(self, n):
        #aquí estic suposant que ho accepto tot, us convenç?
        return n
    
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        print('Doncs ja estarem')
        
        