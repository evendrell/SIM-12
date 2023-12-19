from slam import *
from queue import Queue
from entitat import *
class batch(slamiii):
    
     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(batch, self).__init__(scheduler,parametres)
        #Que faig amb parametres, en aquest cas nop
        self.parametres=parametres
        lista_atributos = parametres.split(',')
        self.n = lista_atributos[0]
        self.action = lista_atributos[1]
        self.m = lista_atributos[2]
        self.nouEstat(Estat.LLIURE)
        self.cola = Queue(maxsize=self.m)
        self.novaEntitat = None
        self.entitatsProcesades = 0
        self.pendents = []
    
    def __repr__(self):
        return "nop"
    
    def actualitzarAtributs(self, entitat):
        #for atributo in entitat.atributs:
        #    print(atributo)
        
        if self.action == "LAST":
            self.novaEntitat.atributs = entitat.atributs

    def gestionarPendents(self, n):
        self.scheduler.afegirEsdeveniment(esdeveniment(self._successor,self.scheduler._tempsSimulacio, TipusEvent.TraspasEntitat, self.novaEntitat, self))

    # se programa el diagrama que hemos hecho
    def tractarEsdeveniment(self, event):
        if self.estat == Estat.LLIURE:
            if event.tipus == TipusEvent.TraspasEntitat:
                # hago cola y aculumo entidades
                self.cola.put(event.entitat)
                self.novaEntitat=entitat()
                self.nouEstat(Estat.BATCHING)
        elif self.estat == Estat.BATCHING:
            if event.tipus == TipusEvent.TraspasEntitat:
                self.actualitzarAtributs(event.entitat) # de self.sortida
                if self.entitatsProcesades == self.m:
                    if self._successor.acceptaEntitat(1):
                        self.scheduler.afegirEsdeveniment(esdeveniment(self._successor,event.tempsExecucio, TipusEvent.TraspasEntitat, self.novaEntitat, self))
                    else:
                        self.pendents.append(self.novaEntitat)
                    self.nouEstat(Estat.LLIURE)

    def iniciSimulacio(self):
        print('Soc nop i he rebut un iniciSimulacio')
        #Jo no he de fer res
        pass
    
    def fiSimulacio(self):
        #Aquí tampoc faig res
        pass
    
    # dir si accepto entitat (en principi tots)
    def acceptaEntitat(self, n):
        #aquí estic suposant que ho accepto tot, us convenç?
        return n
    
    # estaditics quants elements han pasat per aqui i quants hem creat
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        print('Doncs ja estarem')
        
        
