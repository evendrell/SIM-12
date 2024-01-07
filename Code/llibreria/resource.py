from slam import *
from queue import Queue
from entitat import *

class resource(slamiii):
    
     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(resource, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.parametres=parametres
        lista_atributos = parametres.split(',')

        self.n = int(lista_atributos[2])
        self.set_estat(Estat.LLIURE)
        self.cola = Queue(maxsize=self.n)
        self.instancies_disponibles = self.n
    
    def __repr__(self):
        return "resource"

    # se programa el diagrama que hemos hecho
    def tractarEsdeveniment(self, event):
        if self.get_estat() == Estat.LLIURE:

            if event.tipus == TipusEvent.TraspasEntitat:
                if event.prioritat :
                    self.traspassarEntitat(entitat, self._successor)
                else :
                    self.cola.put(entitat)
                    self.instancies_disponibles += 1
                    self.set_estat(Estat.RESOURCING)
        
        elif self.get_estat() == Estat.RESOURCING:
            while not self.cola.empty() and self.instancies_disponibles > 0:
                entitat = self.cola.get()
                self.instancies_disponibles -= 1
                self.traspassarEntitat(entitat, self._successor)
            
            self.set_estat(Estat.LLIURE)

    def iniciSimulacio(self):
        #TODO la classe pare manega el successor
        super(resource, self).iniciSimulacio()
        #TODO posar els estadístics a zero (nombre entitats processades, nombre d'entitas empaquetades)
        pass
    
    def fiSimulacio(self):
        super(resource,self).fiSimulacio()
    
    # dir si accepto entitat (en principi tots)
        


    def acceptaEntitat(self):
        #nomes acceptem entitats si hi caben a la cua
        return self.cola.size() <= self.n 
            
        
    
    # estaditics quants elements han pasat per aqui i quants hem creat
    def summary(self):
        #Mostrar els estadístics per pantalla amb el nom, format desitjat 
        return " EST: "+str(self.estadisticProcessades)+' '+str(self.estadisticCreades)
        
        
        







