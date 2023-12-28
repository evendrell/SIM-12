'''
Doncs aquí estem en l'objecte pare de la vostra jerarquia d'elements pel vostre simulador a mida, basat en SLAM-II
Treballar amb programació orientat a objectes quan desenvolupem un simulador a mida té les seves avantatge:
1.- Reaprofitament de les classes bases, normalment un element que proveeix d'entitats sempre proveirà més o menys de la mateixa, un recurs estarà o no disponible...
2.- Els mètodes abstractes que sobreescrivim en faciliten la comprensió del codi
3.- Alguna proposta més... ?
'''
from enumeracions import *
from esdeveniment import *

#Fa molt que no programo en python, així que potser ho seu seria fer una interficie o alguna cosa d'aquests que feu el jovent...

class slamiii:
    #necessiteu afegir algun métode o propietat a la classe slamiii?
    _estat=None
    _id=-1
    _predecessor=None
    _successor=None
    _traspassosPendents=None
    _surten=0
    x=0
    y=0
    z=0

     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parameters):
        self.set_estat(Estat.LLIURE)
        self._id=int(parameters.split(",")[0])
        self.scheduler=scheduler
        if (self._id >= 2): #No podem tenir predecessors si som la primera instrucció del model.
            self._predecessor=self.scheduler.donamActivitat(self._id-1)   
        self._traspassosPendents=[]     
        
    def __repr__(self):
        assert (False)
        
    def tractarEsdeveniment(self, event):
        #Que ha de fer el vostre element en funció de l'estat en el que es troba i el tipus d'event
        assert (False)    

    #cada cop que crideu aquest métode intenteu enviar una entitat a un destí si aquest té capacitat
    def traspassarEntitat(self,entitat,desti):
        if (desti==None):
            return #No podem enviar res a None
        
        #esdeveniment que programeu que s'inserirà a la llista d'esdeveniment
        traspas=esdeveniment(desti,self.scheduler.temps(),TipusEvent.TraspasEntitat,entitat,self)
        if (desti.acceptaEntitat(1)):
            #En aquest punt li diem al motor que afegeixi l'esdeveniment a la posició que li per toca
            self.scheduler.afegirEsdeveniment(traspas)
            self._surten=self._surten+1
        else:
            #si no puc afegir el guardo per a més tard
            self._traspassosPendents.append(traspas)

    #Si algun objecte us demanava d'enviar-vos una entitat cal que us enrecordeu de qui és per poder després cridar el métode traspasHabilitat de l'objecte implicat
    def traspasHabilitat(self,desti,espai):
        #Cal que busqueu dins la llista de traspassosPendents aquells esdeveniments que tenen el .perA igual a desti
        #doncs destí us diu que té espai lliures, per a cada candidat podeu invocar de nou el traspassarEntitat
        
        #candidat=....
        # candidat.perA==desti traspassarEntitat(candidat.perA,candidat.entitat) i eliminar candidat de la llista

        
        #el temps de simulació que teniu en el candidat s'ha d'actualitzar amb el temps actual de simulació.

        #traspassarEntitat(traspas)
        pass
                
    def iniciSimulacio(self):
        #El vostre element ha de fer quelcom especial quan s'inicia la simulació?
        self._successor=self.scheduler.donamActivitat(self._id+1)
        self.estat=Estat.LLIURE
        self._surten=0
        self.x=0
        self.y=0
        self.z=0
    
    def fiSimulacio(self):
        #El vostre element ha d'invocar el super.fiSimulacio
        self.summary()
    '''
    centralitzar el canvi d'estat us pot anar molt bé per a registrar estadístics i controlar millor el codi
    eviteu fer self._state a qualsevol lloc
    '''
    def set_estat(self,estat):
        self._estat = estat;
    
    def get_estat(self):
        return self._estat;
    
    def set_X(self, value):
        self.x = value;

    def get_X(self):
        return self.x;
    
    def set_Y(self, value):
        self.y = value;

    def get_Y(self):
        return self.y;
    
    def set_Z(self, value):
        self.z = value;

    def get_Z(self):
        return self.z;
    
    
    
    def id(self):
        return self._id;

    def acceptaEntitat(self, n):
        #El vostre element pot acceptar n entitats
        #que retornareu -1, m com a nombre d'entitats que accepteu?
        assert (False)
    
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        print("mnty")
        assert (False)
        
        
