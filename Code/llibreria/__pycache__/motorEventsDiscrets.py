import bisect
from esdeveniment import *
from nopActivity import *

'''
Inicieu el vostre motor de simulació a partir d'aquesta classe

'''
class motorEventsDiscrets:
    _tempsSimulacio = 0
    # hem de tenir una llista amb els esdeveniments ordenats en el temps
    _llistaEsdeveniments = []
    _llistaActivitats = []
    
    def __init__(self):
        primerEsdeveniment=esdeveniment(self,0,TipusEvent.IniciSimulacio,None)
        self._llistaEsdeveniments.append(primerEsdeveniment)
    
    def __repr__(self):
        return "Soc el motor d'esdeveniments discrets"
 
    def run(self):
        self.carregarModel()
        #Sempre iniciem la simulació en temps 0
        self._tempsSimulacio=0        
        #bucle de simulacio (condicio fi simulacio llista buida)
        while len(self._llistaEsdeveniments)>0:
            #recuperem esdeveniment simulacio
            properEsdeveniment=self._llistaEsdeveniments.pop(0)
            #actualitzem el rellotge de simulacio
            self.tempsSimulacio=properEsdeveniment.tempsExecucio;
            # deleguem l'accio a realitzar de l'esdeveniment a l'objecte que l'ha generat
            properEsdeveniment.perA.tractarEsdeveniment(properEsdeveniment)
        
        #recollida d'estadistics
        self.fiSimulacio()

    def afegirEsdeveniment(self,event):
        #inserir esdeveniment de forma ordenada
        bisect.insort(self.eventList, event)
        a=10

    def carregarModel(self):
        '''
        Aquí hauríeu de llegir un arxiu de text i fer el parser que toqui per a instanciar els elements del model
        '''
        #El meu hard-code
        nop = nopActivity(self,"1,NOP,no tinc parametres")
        self._llistaActivitats.append(nop)

    def iniciSimulacio(self):
        self._llistaActivitats[0].iniciSimulacio()

    def tractarEsdeveniment(self,esdevenimentActual):
        if (esdevenimentActual.tipus==TipusEvent.IniciSimulacio):
            self.iniciSimulacio()
    
    def fiSimulacio(self):
        self._llistaActivitats.pop(0).fiSimulacio()

   
   

if __name__ == "__main__":
    elMotor = motorEventsDiscrets()
    elMotor.run()
