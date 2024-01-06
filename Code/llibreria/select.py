from slam import *
from queue import Queue
from entitat import *

class select(slamiii):

    # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(batch, self).__init__(scheduler,parametres)
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
        return "select"


    #Código chorizeado
    def iniciSimulacio(self):
        super(select, self).iniciSimulacio()
        self.entren=0
        self.set_estat(Estat.LLIURE)
        print('Soc nop i he rebut un iniciSimulacio')
        #Jo no he de fer res
        pass
    
    def fiSimulacio(self):
        #Aquí tampoc faig res
        pass
 
    def acceptaEntitat(self, n):
        #aquí estic suposant que ho accepto tot, us convenç?
        return n
    
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        return " EST: "+str(self.entren)+' '+str(self._surten)