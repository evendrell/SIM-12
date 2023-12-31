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
        self.set_estat(Estat.TANCADA) 

        # Inicialitzem estadistics
        self.estadisticEntrades=0
        
        # Inicialitzem llistes per guardar referencies a les entitats
        self.esta_oberta_list = []
    
    def __repr__(self):
        return "gate"
    
    def obrePorta(self):
        self.set_estat(Estat.OBERTA)
        self.esticOberta = True
        self.set_Z(self.z+1)
        self.esta_oberta_list = []
        
    def tancaPorta(self):
        self.set_estat(Estat.TANCADA)
        self.esticOberta = False
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
                # TODO: Revisar funcionament per gestionar referencies a entitats
                self.esta_oberta_list.append(event.desde)
                self.traspassarEntitat(event.entitat,self._successor)
                
            elif event.tipus == TipusEvent.TancarPorta:
                self.tancaPorta()
                  
            elif event.tipus == TipusEvent.TraspasEntitat:
                self.estadisticEntrades += 1;
                self.traspassarEntitat(event.entitat,self._successor)
        elif currentState == Estat.TANCADA:
            if event.tipus == TipusEvent.EstaLaPortaOberta:
                # TODO: Revisar funcionament per gestionar referencies a entitats
                self.esta_oberta_list.append(event.desde)
            
            elif event.tipus == TipusEvent.ObrirPortaEnTTics:
                self.obraPortaEnTTics(event)
                
            elif event.tipus == TipusEvent.ObrirPorta:
                # TODO: Acabar de revisar comportament per enviar esdeveniment de que esticOberta a totes les entitats que han preguntat
                # TODO: Decidir si ho fem amb esdeveniments o directament amb una funció
                self.obrePorta()
                
            elif event.tipus == TipusEvent.TraspasEntitat:
                self.estadisticEntrades += 1;
                self.esta_oberta_list.append(event.desde)

    def iniciSimulacio(self):
        super(gate, self).iniciSimulacio()
        self.estadisticEntrades=0
        self.esta_oberta_list = []
        self.set_estat(Estat.TANCADA) 
        pass
    
    def fiSimulacio(self):
        super(gate,self).fiSimulacio()
    
    def acceptaEntitat(self, n):
        return n
    
    def summary(self):
        return " EST: "+str(self.estadisticEntrades)+' '+str(self._surten) + ' z: '+ str(self.get_Z()) + ' IDs de les entitats que han preguntat: ' + str(self.esta_oberta_list)
            