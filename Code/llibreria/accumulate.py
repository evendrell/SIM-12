from slam import *
from queue import Queue
from entitat import *

class accumulate(slamiii):

     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(accumulate, self).__init__(scheduler,parametres)

        self.parametres=parametres
        lista_atributos = parametres.split(',')
        self.T_tics = int(lista_atributos[2])

        self.set_estat(Estat.LLIURE)
        self.entitatsProcesades = 0
        self.x = 0 # Variable que hay que incrementar
        self.T_tics_left = self.T_tics # Tics que faltan

    def __repr__(self):
        return "accumulate"        
    
    def accumulate(self, entitat):
        # Tiene un valor o es el propio ID?????
        self.x += entitat.get_value()
        self.entitatsProcesades += 1

    def schedule_accumulation_event(self, event):
        # Añado un evento de tiempo para mi entidad para desbloquear el valor de 'X'
        self.scheduler.afegirEsdeveniment(TimeEvent(self.T_tics), self)

    def handle_accumulation(self):
        # Que hago con el valor de X ????????
        return self.x
        
    def tractarEsdeveniment(self, event):
        ''' 
        Si estoy LLIURE y me llega una entidad, me pongo a SERVEI y programo un evento para cuando acabe el tiempo de acumulación. Paso la entidad.
        Si estoy SERVEI y me llega una entidad, la acumulo y paso la entidad
        Si estoy SERVEI y me llega un evento de tiempo, me pongo a LLIURE y envío el valor de 'X'
        '''
        if self.state == 'IDLE':

            if not isinstance(event, entitat):
                return
            
            self.state = 'ACCUMULATING'
            
            self.x = entitat.get_value()
            self.schedule_accumulation_event(event)

        elif self.state == 'ACCUMULATING':
            if isinstance(event, entitat):
                self.accumulate(event)

            elif isinstance(event, TimeEvent):
                self.state = 'IDLE'
                self.handle_accumulation()


    def iniciSimulacio(self):
        super(accumulate, self).iniciSimulacio()
        pass
    
    def fiSimulacio(self):
        super(accumulate, self).fiSimulacio()
        pass

    def acceptaEntitat(self, n):
        self.acceptaEntitat(1)
        pass
    
    # estaditics quants elements han pasat per aqui i quants hem creat
    def summary(self):
        #Mostrar els estadístics per pantalla amb el nom, format desitjat 
        return " EST: "+str(self.entitatsProcesades)+' '+str(self.surten)
    

class TimeEvent:

    def __init__(self, time):
        self.time = time

    def __repr__(self):
        return "TimeEvent" + str(self.time)