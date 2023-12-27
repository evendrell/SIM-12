from slam import *
from queue import Queue
from entitat import *

class queue(slamiii):
    entren=0
    # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(queue, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.parametres=parametres
        lista_atributos = parametres.split(',')
        #Esther t'he corregit l'accés als paràmetres dons els dos primers són l'identificador de l'activitat i el tipus activitat
        #Atenció tots, recordeu a forçar el tipus del paràmetre
        self.cap = int(lista_atributos[2])
        self.m = int(lista_atributos[3])
        self.set_estat(Estat.LLIURE)
        #Esther, al final no necessita la cua per emmagatzemar temporalment les entitats pq sols usem el LAST com a métode d'assignació dels atributs de la nova entitat
        #self.cola = Queue(maxsize=self.m)
        self.novaEntitat = None
        self.entitatsProcesades = 0
        self.estadisticProcessades=0
        self.estadisticCreades=0
        
    def __repr__(self):
        return "nop "+str(self.id())
        
    def tractarEsdeveniment(self, event):
        #Soc nop no importa el meu estat ni el meu event, simplement deixo passar l'entitat cap endavant
        #No està implementada la transferència hauria de ser un esdeveniment amb el temps actual i màxima prioritat
        self.entren=self.entren+1
        self.traspassarEntitat(event.entitat,self._successor)
        pass      

    def iniciSimulacio(self):
        #TODO la classe pare manega el successor
        super(queue, self).iniciSimulacio()
        #TODO posar els estadístics a zero (nombre entitats processades, nombre d'entitas empaquetades)
        pass
    
    def fiSimulacio(self):
        super(queue,self).fiSimulacio()
 
    def acceptaEntitat(self, n):
        #aquí estic suposant que ho accepto tot, us convenç?
        return n
    
    def summary(self):
        #Mostrar els estadístics per pantalla amb el nom, format desitjat 
        return " EST: "+str(self.estadisticProcessades)+' '+str(self.estadisticCreades)
        
        
