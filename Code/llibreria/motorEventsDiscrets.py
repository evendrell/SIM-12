import bisect
from esdeveniment import *
from nopActivity import *
from blockActivity import *
from batch import *

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
        bisect.insort(self._llistaEsdeveniments, event)
        a=10

    def donamActivitat(self,index):
        if (index < len(self._llistaActivitats)):
            return None
        else:
            return self._llistaActivitats[index]
    
    def carregarModel(self):
        index=0
        with open('llibreria/model.txt') as f:
            linia = f.readline()
            activitat=self.instanciar(str(index)+","+linia)
            self._llistaActivitats.append(activitat)
            index=index+1
            #Aquest codi és pot millorar segur, però cadascú hauria de poder identificar el nom de la seva activitat
       
    def temps(self):
        return self._tempsSimulacio
    
    #A completar per cadascun de vosaltres, potser trobeu alguna opció més bònica de fer-ho.
    def instanciar(self,activitat):
        element=None
        if 'batch' in activitat:
            element=batch(self,activitat)
        if 'nop' in activitat:
            element=nopActivity(self,activitat)
        if 'block' in activitat:
            element=blockActivity(self,activitat)
        return element
    
    def iniciSimulacio(self):
        self._llistaActivitats[0].iniciSimulacio()

    def tractarEsdeveniment(self,esdevenimentActual):
        if (esdevenimentActual.tipus==TipusEvent.IniciSimulacio):
            self.iniciSimulacio()
            #programo tres events d'arribada pel batch de prova
            self.afegirEsdeveniment(esdeveniment(self._llistaActivitats[0],0,TipusEvent.TraspasEntitat,entitat(),0,0))
            self.afegirEsdeveniment(esdeveniment(self._llistaActivitats[0],1,TipusEvent.TraspasEntitat,entitat(),0,0))
            self.afegirEsdeveniment(esdeveniment(self._llistaActivitats[0],2,TipusEvent.TraspasEntitat,entitat(),0,0))
    
    def fiSimulacio(self):
        self._llistaActivitats.pop(0).fiSimulacio()

   
   

if __name__ == "__main__":
    elMotor = motorEventsDiscrets()
    elMotor.run()
