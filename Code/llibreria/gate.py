from slam import *
from entitat import *

class gate(slamiii):
    
    def __init__(self,scheduler,parametres):
        super(gate, self).__init__(scheduler,parametres)

        # Dividim els parametres en una llista per poder accedir més fàcilment
        self.parametres=parametres
        parametres_list = parametres.split(',')

        # Nombre de tics
        self.T = int(parametres_list[2])

        # Actualitzem estat inicial
        self.set_estat(Estat.OBERTA)

        # Inicialitzem estadistics
        self.estadisticEntrades=0
        
        # Inicialitzem llistes per guardar referencies dels objectes que han demana si la porta esta oberta
        self.esta_oberta_list = []
        
        # Inicialitzem llistes per guardar referencies de les entitats que han demanat traspas
        self.entitats_list = []
    
    def __repr__(self):
        return "gate"
    
    def obrePorta(self):
        self.set_estat(Estat.OBERTA)
        self.set_Z(self.z+1)
        for objecteSim in self.esta_oberta_list:
           traspas=esdeveniment(perA=objecteSim,temps=self.scheduler.temps(),tipus=TipusEvent.EsticOberta,entitat=None,desde=self, prioritat=0)
           self.scheduler.afegirEsdeveniment(traspas)
        
        for objecteSim in self.entitats_list:
            objecteSim.traspasHabilitat(self, 999)
    
        self.esta_oberta_list = []
        self.entitats_list = []
        
    def tancaPorta(self):
        self.set_estat(Estat.TANCADA)
        self.set_Z(self.z+1)
        
    def esticOberta(self):
        return self.get_estat() == Estat.OBERTA
        
    def obraPortaEnTTics(self, event):        
        traspas=esdeveniment(perA=self,temps=self.scheduler.temps()+self.T,tipus=TipusEvent.ObrirPorta,entitat=event.entitat,desde=self)
        self.scheduler.afegirEsdeveniment(traspas)
    
    # Codifiquem el diagrama SDL
    def tractarEsdeveniment(self, event):
        currentState = self.get_estat()
        
        if currentState == Estat.OBERTA:
            if event.tipus == TipusEvent.EstaLaPortaOberta:
                traspas=esdeveniment(perA=event.desde,temps=self.scheduler.temps(),tipus=TipusEvent.EsticOberta,entitat=event.entitat,desde=self, prioritat=0)
                self.scheduler.afegirEsdeveniment(traspas)
                
            elif event.tipus == TipusEvent.TancarPorta:
                self.tancaPorta()
                  
            elif event.tipus == TipusEvent.TraspasEntitat:
                self.estadisticEntrades += 1

                self.traspassarEntitat(event.entitat,self._successor)

        elif currentState == Estat.TANCADA:
            if event.tipus == TipusEvent.EstaLaPortaOberta:
                self.esta_oberta_list.append(event.desde)
            
            elif event.tipus == TipusEvent.ObrirPortaEnTTics:
                self.obraPortaEnTTics(event)
                
            elif event.tipus == TipusEvent.ObrirPorta:
                self.obrePorta()
                
            elif event.tipus == TipusEvent.TraspasEntitat:
                self.estadisticEntrades += 1;
                self.entitats_list.append(event.desde)

    def iniciSimulacio(self):
        super(gate, self).iniciSimulacio()
        self.estadisticEntrades=0
        self.esta_oberta_list = []
        self.entitats_list = []
        self.set_estat(Estat.OBERTA)
        pass
    
    def fiSimulacio(self):
        super(gate,self).fiSimulacio()
    
    def acceptaEntitat(self, n):
        return self.get_estat() == Estat.OBERTA
    
    def summary(self):
        return " EST: "+str(self.estadisticEntrades)+' '+str(self._surten) + ' z: '+ str(self.get_Z()) + ' IDs de preguntat: ' + str(self.esta_oberta_list) + ' IDs de traspas: ' + str(self.entitats_list)
            