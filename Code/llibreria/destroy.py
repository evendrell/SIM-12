from slam import *
from queue import Queue
from entitat import entitat
from motorEventsDiscrets import *

class destroy(slamiii):

    def __init__(self,scheduler,T_tics):
        super(destroy, self).__init__(scheduler,T_tics)

        self.T_tics=T_tics

        self.set_estat(Estat.LLIURE)
        self.T_tics_left = self.T_tics # Tics que falten
        self.entity_queue = Queue()

    def __repr__(self):
        return "destroy"        
    
    def destroy(self, entitat):
        self.y = slamiii.get_Y(slamiii)
        self.y += 1
        slamiii.set_Y(slamiii, self.y)
        slamiii.set_estat(slamiii, Estat.DESTROYED)

    # Se programa el evento de fin de destroy
    def schedule_destroy_event(self, event):
        T_tics = event.tempsExecucio + self.T_tics_left
        motorEventsDiscrets.afegirEsdeveniment(esdeveniment(self, T_tics, TipusEvent.Timer))
        
    # Trabajo propio del componente
    def tractarEsdeveniment(self, event):
        if self.get_estat() == Estat.LLIURE:
            
            self.set_estat(Estat.SERVEI)

            self.schedule_destroy_event(self, event)
            self.destroy(event.entitat)
            
        elif self.get_estat() == Estat.SERVEI:

            if event.tipus == TipusEvent.TraspasEntitat:
                self.add_queue_entity(self, event.entitat)
            else:
                self.destroy(self, event.entitat)
                if (self.entity_queue.qsize() > 0):
                    entitat = self.entity_queue.get()
                    self.schedule_destroy_event(self, event)
                    self.destroy(self, entitat)
                else:
                    self.set_estat(Estat.LLIURE)
                
    def iniciSimulacio(self):
        super(destroy, self).iniciSimulacio()
        pass
    
    def fiSimulacio(self):
        super(destroy, self).fiSimulacio()
        pass

    def acceptaEntitat(self, n):
        self.acceptaEntitat(n)
        pass
    
    def add_queue_entity(self, entitat):
        self.entity_queue.put(entitat)
    
    def summary(self):
        return " "
    
    