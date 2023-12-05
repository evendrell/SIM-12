import bisect
from Event import *
from Gainn import *
from Gata import *
from Gaut import *
from Politie import *

class SimuleringsMotor:

    currentTime = 0
    # hem de tenir una llista amb els esdeveniments ordenats en el temps
    eventList = []
    
    def __init__(self):
    
        self.simulationStart=Event(self,0,EventType.SimulationStart,None)
        self.eventList.append(self.simulationStart)
        self.tempsSimulacio=100
        self.arrivaltimes=2
        self.cycletimes=10
        self.passVehicles=3
        self.veuretraza=0
    
    def __repr__(self):
        return "Simulerings Motor"
 
    def run(self):
        #configurar el model per consola, arxiu de text...
        self.configurar()
        self.crearModel()
        
        #rellotge de simulacio a 0
        self.currentTime=0        
        #bucle de simulacio (condicio fi simulacio llista buida)
        while self.currentTime<self.tempsSimulacio:
            #recuperem event simulacio
            event=self.eventList.pop(0)
            #actualitzem el rellotge de simulacio
            self.currentTime=event.tid
            self.trace(event)
            # deleguem l'accio a realitzar de l'esdeveniment a l'objecte que l'ha generat
            # tambe podriem delegar l'accio a un altre objecte
            event.objekt.tractarEsdeveniment(event)
        
        #recollida d'estadistics
        self.recollirEstadistics()

    def trace(self,event):
        if (self.veuretraza==0):
             return
        color=Colors.HEADER
        if event.type==EventType.Access:
            color=Colors.OKBLUE
        if event.type==EventType.Cycle:
            color=Colors.HEADER
        if event.type==EventType.NextArrival:
            color=Colors.OKGREEN
        if event.type==EventType.StepIn:
            color=Colors.OKCYAN
        if event.type==EventType.Tranfer:
            color=Colors.OKRARO
        print(color,event.tid,event.type,' ',event.objekt,Colors.ENDC)

    def afegirEsdeveniment(self,event):
        #inserir esdeveniment de forma ordenada
        bisect.insort(self.eventList, event)
        a=10


    def tractarEsdeveniment(self,event):
        if (event.type==EventType.SimulationStart):
            self.gainn.simulationStart()
            self.polite.simulationStart()
            self.gataO.simulationStart()
            self.gataE.simulationStart()
            self.gataN.simulationStart()
            self.gataS.simulationStart()
            self.gaut.simulationStart()
    
    # instanciar todas las clases
    def configurar(self):
        print('Demanar parametres del simulador de policia ')
        error=True
        while error:
            self.tempsSimulacio=(float)(input("Temps Simulacio: "))
            self.arrivaltimes=(float)(input("Temps entre arribades: "))
            self.cycletimes=(float)(input("Temps de cicle del guardia: "))
            self.passVehicles=(float)(input("Temps de pas dels vehicles: "))
            self.veuretraza=(int)(input("Veure Events, prem 0 per no veure els events: "))
            if (self.passVehicles>self.cycletimes):
                print('El pas de vehicles ha de ser inferior al temps de cicle del guardia')
            else:
                error=False

    def crearModel(self):
        # creacio dels objectes que composen el meu model
        self.gainn = Gainn(self,self.arrivaltimes)
        self.polite = Politie(self,self.cycletimes)
        self.gataO = Gata(self,'ost',State.LOCK,self.passVehicles,self.veuretraza)
        self.gataE = Gata(self,'Vest',State.UNLOCK,self.passVehicles,self.veuretraza)
        self.gataN = Gata(self,'Nord',State.LOCK,self.passVehicles,self.veuretraza)
        self.gataS = Gata(self,'Sor',State.LOCK,self.passVehicles,self.veuretraza)
        self.gaut = Gaut(self.veuretraza)

        self.gainn.koble(self.gataO,self.gataE,self.gataS,self.gataN)
        self.polite.koble(self.gataO,self.gataE,self.gataS,self.gataN)

        self.gataO.koble(self.gaut)
        self.gataE.koble(self.gaut)
        self.gataN.koble(self.gaut)
        self.gataS.koble(self.gaut)

    def recollirEstadistics(self):
        print(Colors.HEADER,"ESTADÍSTICS",Colors.ENDC)

        self.gainn.summary()
        self.gataO.summary()
        self.gataE.summary()
        self.gataN.summary()
        self.gataS.summary()
        self.polite.summary()
        self.gaut.summary()
   

if __name__ == "__main__":
    scheduler = SimuleringsMotor()
    scheduler.run()
