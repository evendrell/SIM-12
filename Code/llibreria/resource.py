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
        #Esther t'he corregit l'accés als paràmetres dons els dos primers són l'identificador de l'activitat i el tipus activitat
        #Atenció tots, recordeu a forçar el tipus del paràmetre
        self.n = int(lista_atributos[2])
        self.action = lista_atributos[3]
        self.m = int(lista_atributos[4])
        self.set_estat(Estat.LLIURE)
        #Esther, al final no necessita la cua per emmagatzemar temporalment les entitats pq sols usem el LAST com a métode d'assignació dels atributs de la nova entitat
        #self.cola = Queue(maxsize=self.m)
        self.novaEntitat = None
        self.entitatsProcesades = 0
        self.estadisticProcessades=0
        self.estadisticCreades=0
    
    def __repr__(self):
        return "resource"
    
    def actualitzarAtributs(self, entitat):
        if self.action == "LAST":
            self.novaEntitat.atributs = entitat.atributs

    # se programa el diagrama que hemos hecho
    def tractarEsdeveniment(self, event):
        ''' 
        El tractament d'esdeveniments és la codificació del diagrama de processos, podeu fer com l'Esther i preguntar per a cada 
        estat que s'ha de fer quan es rep un esdeveniment.
        '''
        if self.get_estat() == Estat.LLIURE:
            if event.tipus == TipusEvent.TraspasEntitat:
                #Esther no et cat ja fer servir la cua
                # hago cola y aculumo entidades
                #self.cola.put(event.entitat)
                self.novaEntitat=entitat()
                self.entitatsProcesades=1
                self.estadisticProcessades=self.estadisticProcessades+1
                self.set_estat(Estat.RESOURCING)
                #TODO aquí hauries de comprovar que no tinguis el paquet ja fet (i modificar el diagrama de processos) podria donar-se el cas de que et diu fer un batch amb una sola entitat.
        
        elif self.get_estat() == Estat.RESOURCING:
            if event.tipus == TipusEvent.TraspasEntitat:
                self.actualitzarAtributs(event.entitat) # de self.sortida
                self.entitatsProcesades=self.entitatsProcesades+1
                self.estadisticProcessades=self.estadisticProcessades+1
                if self.entitatsProcesades == self.n:
                    self.estadisticCreades=self.estadisticCreades+1
                    #Arribat aquest punt, he processat n entitats, el batch ja pot provar d'enviar l'entitat cap al seu successor
                    self.traspassarEntitat(self.novaEntitat,self._successor)
                    #Esther ho he promogut a la classe pare pq tothom pugui fer el mateix, ja fareu net el codi.
                    #if self._successor.acceptaEntitat(1):
                    #    self.scheduler.afegirEsdeveniment(esdeveniment(self._successor,event.tempsExecucio, TipusEvent.TraspasEntitat, self.novaEntitat, self))
                    #else:
                    #    self.pendents.append(self.novaEntitat)
                    self.set_estat(Estat.LLIURE)

    def iniciSimulacio(self):
        #TODO la classe pare manega el successor
        super(resource, self).iniciSimulacio()
        #TODO posar els estadístics a zero (nombre entitats processades, nombre d'entitas empaquetades)
        pass
    
    def fiSimulacio(self):
        super(resource,self).fiSimulacio()
    
    # dir si accepto entitat (en principi tots)
    def acceptaEntitat(self, n):
        #aquí estic suposant que ho accepto tot, us convenç?
        return n
    
    # estaditics quants elements han pasat per aqui i quants hem creat
    def summary(self):
        #Mostrar els estadístics per pantalla amb el nom, format desitjat 
        return " EST: "+str(self.estadisticProcessades)+' '+str(self.estadisticCreades)
        
        
        
