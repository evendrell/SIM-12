from slam import *
from queue import Queue
from entitat import entitat
from motorEventsDiscrets import *

class accumulate(slamiii):

    # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(accumulate, self).__init__(scheduler,parametres)

        self.parametres=parametres
        llista_atributs = parametres.split(',')

        self.atr = int(llista_atributs[0])
        self.T_tics = int(llista_atributs[1])
        self.M = int(llista_atributs[2])

        self.set_estat(Estat.LLIURE)
        self.entitatsProcesades = 0
        self.x = 0 # Variable que hay que incrementar
        self.T_tics_left = self.T_tics # Tics que faltan

    def __repr__(self):
        return "accumulate"        
    
    # Se acumula el valor de 'X'
    def accumulate(self, entitat):
        self.x += entitat.get_atribut(self.atr)
        self.entitatsProcesades += 1

    # Se programa el evento de fin de acumulación
    def schedule_accumulation_event(self, event):
        T_tics = event.tempsExecucio + self.T_tics_left
        motorEventsDiscrets.afegirEsdeveniment(esdeveniment(self, T_tics, TipusEvent.Timer))

    # Se actualiza el valor de 'X'
    def handle_accumulation(self):
        self._X = self.x
        
    # Trabajo propio del componente
    def tractarEsdeveniment(self, event):
        ''' 
        Si estoy LLIURE y me llega una entidad, me pongo a SERVEI y programo un evento para cuando acabe el tiempo de acumulación. Paso la entidad.
        Si estoy SERVEI y me llega una entidad, la acumulo y paso la entidad
        Si estoy SERVEI y me llega un evento de tiempo, me pongo a LLIURE y envío el valor de 'X'
        '''
        if self.get_estat() == Estat.LLIURE:
            
            self.set_estat(Estat.SERVEI)
            
            self.schedule_accumulation_event(event)
            self.accumulate(event.entitat)
            self.traspassarEntitat(event.entitat, self._successor)

        elif self.get_estat() == Estat.SERVEI:

            if event.tipus == TipusEvent.TraspasEntitat:
                self.accumulate(event.entitat)
                self.traspassarEntitat(event.entitat, self._successor)
            else:
                # 'T' tics, modifico valor de 'x'
                self.handle_accumulation()
                self.set_estat(Estat.LLIURE)
                


    def iniciSimulacio(self):
        super(accumulate, self).iniciSimulacio()
        pass
    
    def fiSimulacio(self):
        super(accumulate, self).fiSimulacio()
        pass

    def acceptaEntitat(self, n):
        self.acceptaEntitat(n)
        pass
    
    # estaditics quants elements han pasat per aqui i quants hem creat
    def summary(self):
        #Mostrar els estadístics per pantalla amb el nom, format desitjat 
        return " EST: "+str(self.entitatsProcesades)+' '+str(self._surten)
    
    