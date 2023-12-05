from oppregninger import *
import math
from Event import *
from Bil import * 

class Gainn:

    def __init__(self,scheduler,parameter):
        # inicialitzar element de simulacio
        self.entitatsCreades=0
        self.state=State.SERVICE
        self.scheduler=scheduler
        self.parameter=parameter
        self.gater=[]

    def __repr__(self):
        return "Ga inn"
    
    def koble(self,gataE,gataO,gataN,gataS):
        self.gataE=gataE
        self.gataO=gataO
        self.gataN=gataN
        self.gataS=gataS   
        self.gater=[self.gataE,self.gataO,self.gataN,self.gataS]

    def tractarEsdeveniment(self, event):
        if (event.type==EventType.NextArrival):
            self.processNextArrival(event)        

    def simulationStart(self):
        self.entitatsCreades=0
        self.properaArribada(0)
        
    def processNextArrival(self,event):
        #programacio propera arribada
        self.properaArribada(event.tid)
        # incrementem estadistics si s'escau
        self.entitatsCreades=self.entitatsCreades+1
        #creacio entitat arribada
        entitat=Bil(event.tid)
        self.scheduler.afegirEsdeveniment(Event(self.gater[entitat.carrer],event.tid,EventType.Tranfer, entitat))

    def properaArribada(self, temps):
        # cada quan generem una arribada (hauriem de tenir com a minim alguna component estocastica)
        tempsEntreArribades = self.parameter
        # programacio arribada
        self.scheduler.afegirEsdeveniment(Event(self,temps+tempsEntreArribades,EventType.NextArrival, None))
      
    def summary(self):
        print('Entitats arribades al sistema: ',self.entitatsCreades)
        