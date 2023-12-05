from oppregninger import *
import math
import random
from Event import *
from Bil import * 

class Politie:

    def __init__(self,scheduler,parameter):
        # inicialitzar element de simulacio
        self.state=State.ACCESSE
        self.scheduler=scheduler
        self.tempsCicle=parameter
        self.ciclesTotals=0
        self.gater=[]
    
    def __repr__(self):
        return "Politimannen"
    
    def koble(self,gataE,gataO,gataN,gataS):
        self.gataE=gataE
        self.gataO=gataO
        self.gataN=gataN
        self.gataS=gataS   
        self.gater=[self.gataE,self.gataO,self.gataN,self.gataS]

    def tractarEsdeveniment(self, event):
        if (event.type==EventType.Access):
            if (self.state==State.ACCESSE):
                self.state=State.ACCESSS    
                self.scheduler.afegirEsdeveniment(Event(self.gataE,event.tid,EventType.Access,None))
                self.scheduler.afegirEsdeveniment(Event(self.gataS,event.tid,EventType.Access,None))
            elif (self.state==State.ACCESSS):
                self.state=State.ACCESSO    
                self.scheduler.afegirEsdeveniment(Event(self.gataS,event.tid,EventType.Access,None))
                self.scheduler.afegirEsdeveniment(Event(self.gataO,event.tid,EventType.Access,None))
            elif (self.state==State.ACCESSO):
                self.state=State.ACCESSN    
                self.scheduler.afegirEsdeveniment(Event(self.gataO,event.tid,EventType.Access,None))
                self.scheduler.afegirEsdeveniment(Event(self.gataN,event.tid,EventType.Access,None))
            elif (self.state==State.ACCESSN):
                self.state=State.ACCESSE    
                self.scheduler.afegirEsdeveniment(Event(self.gataN,event.tid,EventType.Access,None))
                self.scheduler.afegirEsdeveniment(Event(self.gataE,event.tid,EventType.Access,None))

            self.scheduler.afegirEsdeveniment(Event(self,event.tid+self.tempsCicle,EventType.Access,None))
            self.ciclesTotals=self.ciclesTotals+1

    def simulationStart(self):
        self.state=State.ACCESSS
        self.scheduler.afegirEsdeveniment(Event(self,self.tempsCicle,EventType.Access,True))
        self.ciclesTotals=0
    
    def summary(self):
        print('Nombre de cicles realitzats pel ',self,': ',self.ciclesTotals)
    


