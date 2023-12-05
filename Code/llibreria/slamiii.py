'''
Doncs aquí estem en l'objecte pare de la vostra jerarquia d'elements pel vostre simulador a mida, basat en SLAM-II
Treballar amb programació orientat a objectes quan desenvolupem un simulador a mida té les seves avantatge:
1.- Reaprofitament de les classes bases, normalment un element que proveeix d'entitats sempre proveirà més o menys de la mateixa, un recurs estarà o no disponible...
2.- Els mètodes abstractes que sobreescrivim en faciliten la comprensió del codi
3.- Alguna proposta més... ?
'''
from enumeracions import *

#Fa molt que no programo en python, així que potser ho seu seria fer una interficie o alguna cosa d'aquests que feu el jovent...

class slamiii:
    #necessiteu afegir algun métode o propietat a la classe slamiii?
    _estat =Estat.LLIURE
    _id=-1

     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parameters):
        self.estat=Estat.LLIURE
        self._id=parameters.split(",")[0]
        self.scheduler=scheduler
        
    def __repr__(self):
        assert (False)
        
    def tractarEsdeveniment(self, event):
        #Que ha de fer el vostre element en funció de l'estat en el que es troba i el tipus d'event
        assert (False)        

    def iniciSimulacio(self):
        #El vostre element ha de fer quelcom especial quan s'inicia la simulació?
        self.estat=Estat.LLIURE
    
    def fiSimulacio(self):
        #El vostre element ha de fer quelcom especial quan acaba la simulació
        assert (False)
    '''
    centralitzar el canvi d'estat us pot anar molt bé per a registrar estadístics i controlar millor el codi
    eviteu fer self._state a qualsevol lloc
    '''
    def estat(self):
        return self._estat;

    def nouEstat(self,estat):
        self._estat = estat;

    def id(self):
        return self._id;

    def acceptaEntitat(self, n):
        #El vostre element pot acceptar n entitats
        #que retornareu -1, m com a nombre d'entitats que accepteu?
        assert (False)
    
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        assert (False)
        
        
