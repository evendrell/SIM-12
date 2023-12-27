from slam import *
from queue import Queue
from entitat import *

class alter(slamiii):
    
     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(alter, self).__init__(scheduler,parametres)
        self.parametres=parametres
        lista_atributos = parametres.split(',')
        #els dos primers parametres són l'identificador de l'activitat i el tipus activitat

        self.n = int(lista_atributos[2])
        self.m = int(lista_atributos[4])
        self.tick_count = 0  # comptador de ticks
        self.set_estat(Estat.LLIURE)

        self.parametres=parametres
        
        self.cola = Queue(maxsize=self.m)

        self.entitatsProcesades = 0
        self.estadisticProcessades=0
        self.self.entitatsGenerades = 0


    def __repr__(self):
        return "alter"
        
    def tractarEsdeveniment(self, event):
        if self.get_estat() == Estat.LLIURE:
            if event.tipus == TipusEvent.Tick:
                self.tick_count += 1
                if self.tick_count == 1:
                    self.set_estat(Estat.MODIFICANT)
                elif self.tick_count == 2:
                    #Creació de M entitats
                    for i in range(self.m):
                        self.novaEntitat = entitat()
                        self.traspassarEntitat(self.novaEntitat,self._successor)     
                        self.entitatsGenerades += 1     
                    self.set_estat(Estat.LLIURE)
            self.cola.put(event.entitat)
        

    def iniciSimulacio(self):
        super(alter, self).iniciSimulacio()
        self.tick_count = 0
        pass
    
    def fiSimulacio(self):
        self.summary()
        pass
 
    def acceptaEntitat(self, n):
        #aquí estic suposant que ho accepto tot, us convenç?
        return n
    
    def summary(self):
         #Mostrar els estadístics per pantalla amb el nom, format desitjat 
        print(Colors.OKBLUE,self,Colors.ENDC,self.estadisticProcessades,' ',self.estadisticCreades)
        
        
