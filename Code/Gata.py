#millor treballar amb define o algun sistema simular a l'enum de C++
from oppregninger import *
from Event import *

class Gata:

    def __init__(self,scheduler,direccio,state,pasdevehicles,veuretraza):
        # inicialitzar element de simulacio
        self.entitatsArribades=0
        self.scheduler=scheduler
        self.entitatActiva=None
        self.schedullerStepIn=False
        self.direccio=direccio
        self.veuretraza=veuretraza
        self.pasdeVehicles=pasdevehicles
        self.biler=[]
        self.setState(state)
        
    def __repr__(self):
        if (self.veuretraza==0):
            return self.direccio+"gata"
        else:
            return self.direccio+"gata"+' '+self.stateStr()
    
    def stateStr(self):
        if self.state==State.LOCK:
            return "lukket"
        else:
            return "apen"

    def setState(self,state):
        self.state=state
        if self.veuretraza==0:
            return
        print('\t\t',Colors.OKBLUE,self,Colors.ENDC)

    def koble(self,gaut):
        self.gaut=gaut
    
    def tractarEsdeveniment(self, event):
        if (self.state==State.LOCK):
            self.tractarEsdevenimentLOCK(event)
        else:
            self.tractarEsdevenimentUNLOCK(event)
        
    def simulationStart(self):
        self.entitatsArribades=0

    def tractarEsdevenimentLOCK(self,event):
        if event.type==EventType.Access:
            if not self.schedullerStepIn:
                self.programarProperStepin(event)
            self.setState(State.UNLOCK)
                    
        if event.type==EventType.Tranfer:
            self.biler.append(event.entitat)
            self.entitatsArribades=self.entitatsArribades+1          

    def tractarEsdevenimentUNLOCK(self,event):
        if event.type==EventType.Access:
            self.setState(State.LOCK)
            
        if event.type==EventType.Tranfer:
            if not self.schedullerStepIn:
                self.programarProperStepin(event)
            self.biler.append(event.entitat)
            self.entitatsArribades=self.entitatsArribades+1

        if event.type==EventType.StepIn:
            if (len(self.biler)>0):
                bilen=self.biler.pop(0)
                self.programarTransfer(event,bilen)                
                self.programarProperStepin(event)
            else:
                self.schedullerStepIn=False                
            

    def programarTransfer(self,event,bilen):
        event= Event(self.gaut,event.tid,EventType.Tranfer,bilen,self)
        self.scheduler.afegirEsdeveniment(event)

    def programarProperStepin(self,event):
        self.schedullerStepIn=True
        event= Event(self,event.tid+self.pasdeVehicles,EventType.StepIn,None)
        self.scheduler.afegirEsdeveniment(event)
    
    def summary(self):
        print(Colors.OKGREEN,self,Colors.ENDC)
        print('\tEntitats arribades: ',self.entitatsArribades)
        print('\tEntitats encuades: ',len(self.biler))