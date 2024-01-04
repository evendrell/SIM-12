from slam import *
from entitat import *

class detect(slamiii):
    def __init__(self,scheduler,parametres):
        super(detect, self).__init__(scheduler,parametres)
        
        self.parametres=parametres
        parameters_list = parametres.split(',')
        self.T = int(parameters_list[2])
        self.VAL = int(parameters_list[3])
        self.M = int(parameters_list[4])
        
        self.estadisticEntrades=0
        self.estadisticSortides=0
        
        self.set_estat(Estat.LLIURE)
  
        
    def __repr__(self):
        return "detect "+str(self.id())
        
    def tractarEsdeveniment(self, event):
        self.estadisticEntrades=self.estadisticEntrades+1
        
        state = self.get_estat()
        
        if state == Estat.LLIURE and event.tipus == TipusEvent.TraspasEntitat:
            if slamiii.get_Z(slamiii) == self.VAL:
                slamiii.set_Z(slamiii, 0)
                self.createMEntitiesInTTicks(event)   
                self.processaEntitats(total=1, entitats=[event.entitat], estatACambiar=Estat.SERVEI)                                              
            
            else:
                self.processaEntitats(total=1, entitats=[event.entitat], estatACambiar=Estat.LLIURE)
                            
        elif state == Estat.SERVEI and event.tipus == TipusEvent.CreaMentitats:
            entitats = []
            for i in range(self.M):
                entitats.append(entitat())
            self.processaEntitats(total=self.M, entitats=entitats, estatACambiar=Estat.LLIURE)         

        else:
            self.traspassarEntitat(event.entitat,self._successor)


    def createMEntitiesInTTicks(self, event):        
        traspas=esdeveniment(perA=self,temps=self.scheduler.temps()+self.T,tipus=TipusEvent.CreaMentitats,entitat=event.entitat,desde=self)
        self.scheduler.afegirEsdeveniment(traspas)

    def processaEntitats(self, total, entitats, estatACambiar):
        self.estadisticSortides=self.estadisticSortides+total 
        for entitat in entitats:
            self.traspassarEntitat(entitat, self._successor)
        self.set_estat(estatACambiar)

    def iniciSimulacio(self):
        super(detect, self).iniciSimulacio()
        self.estadisticEntrades=0
        self.estadisticSortides=0
        pass
    
    def fiSimulacio(self):
        self.summary()
        super(detect, self).fiSimulacio()
        pass
 
    def acceptaEntitat(self, n):
        return n
    
    def summary(self):
        return " EST: "+str(self.estadisticEntrades)+' '+str(self.estadisticSortides) + ' z: ' + str(slamiii.get_Z(slamiii))
        
        
