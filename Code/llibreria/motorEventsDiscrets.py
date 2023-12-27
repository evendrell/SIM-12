import bisect
from esdeveniment import *
from nopActivity import *
from blockActivity import *
from batch import *
import unicurses as curses
import time


'''
Inicieu el vostre motor de simulació a partir d'aquesta classe
'''

class motorEventsDiscrets:
    _tempsSimulacio = 0
    # hem de tenir una llista amb els esdeveniments ordenats en el temps
    _llistaEsdeveniments = []
    _llistaActivitats = []
    debug=False
    milisegons=float(0.0250)
    
    def __init__(self):
        primerEsdeveniment=esdeveniment(self,0,TipusEvent.IniciSimulacio,None)
        self._llistaEsdeveniments.append(primerEsdeveniment)
    
    def __repr__(self):
        return "Soc el motor d'esdeveniments discrets"
 

    def renderPrograma(self,stdscr,executare): 
        stdscr.addstr(1,1,"Model en execució",curses.color_pair(4))   
        stdscr.addstr(2,1,("Temps   Actual: {}").format(self._tempsSimulacio),curses.color_pair(1))
        eventsProgramats=  "Events encuats: "+str(len(self._llistaEsdeveniments))
        stdscr.addstr(3,1, eventsProgramats,curses.color_pair(1))
        
        noColor=True
        if (executare.tipus==TipusEvent.IniciSimulacio or executare.tipus==TipusEvent.FiSimulacio):
            noColor=False

        y=5
        i=-1     

        stdscr.addstr(y,1, "ESTAT",curses.color_pair(5))           
        stdscr.addstr(y,25, "ACTIVITAT",curses.color_pair(5))
        stdscr.addstr(y,50, "ESTADISTIC (entren, surten)",curses.color_pair(5))
        
        y=7
        for instruccio in self.programa:
            i=i+1
            if (noColor and executare.perA.id()==i):
                index=1
            else:
                index=4
            
            
            stdscr.addstr(y+i,25, instruccio,curses.color_pair(index))
            stdscr.addstr(y+i,50, self._llistaActivitats[i].summary(),curses.color_pair(index))
            stdscr.addstr(y+i,1, str(self._llistaActivitats[i].get_estat()).capitalize(),curses.color_pair(index))           

    def renderStatus(self,stdscr,height,width,executare,first):
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(1, width-30, "         SLAM III",curses.color_pair(1))
        stdscr.addstr(2, width-30, "        SIM 23/24",curses.color_pair(2))
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)
        if first:
            statusbarstr = "Prem 'd' per a executar pas a pas"
        else:
            statusbarstr = ("Prem 'd' per executar l'event de tipus {} que succeirà en l'instant {}").format(executare.tipus,executare.tempsExecucio)
        stdscr.attron(curses.color_pair(6))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(6))
        
    def nextStep(self,stdscr,executare,dbg):
        k = 0
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        self.renderPrograma(stdscr,executare)
        first=dbg and not self.debug
        self.renderStatus(stdscr,height,width,executare,first)
        stdscr.refresh()

        # Demanem el següent pas si venim en mode debug
        if (dbg):
            k = stdscr.getch()
            self.debug=(k==100)
        else:
            time.sleep(self.milisegons)

    def run(self,stdscr):
        self.carregarModel()
        #Sempre iniciem la simulació en temps 0
        self._tempsSimulacio=0       
        self.nextStep(stdscr,self._llistaEsdeveniments[0],True)
        #bucle de simulacio (condicio fi simulacio llista buida)
        while len(self._llistaEsdeveniments)>0:
            #recuperem esdeveniment simulacio
            properEsdeveniment=self._llistaEsdeveniments.pop(0)
            # sols per entendre com funciona el simulador d'esdeveniments discrets
            self.nextStep(stdscr,properEsdeveniment,self.debug)
            #actualitzem el rellotge de simulacio
            self._tempsSimulacio=properEsdeveniment.tempsExecucio;
            # deleguem l'accio a realitzar de l'esdeveniment a l'objecte que l'ha generat
            properEsdeveniment.perA.tractarEsdeveniment(properEsdeveniment)
            
        
        #recollida d'estadistics
        self.fiSimulacio()
        self.nextStep(stdscr,esdeveniment(self,self._tempsSimulacio,TipusEvent.FiSimulacio,None,None),True)

    def afegirEsdeveniment(self,event):
        if (event.tempsExecucio<self._tempsSimulacio):
            #no podem inserir un esdeveniment d'un temps ja passat
            assert(False)
        #inserir esdeveniment de forma ordenada
        bisect.insort(self._llistaEsdeveniments, event)
        a=10

    def donamActivitat(self,index):
        if (index >= len(self._llistaActivitats)):
            return None
        else:
            return self._llistaActivitats[index]
    
    def carregarModel(self):
        index=0
        self.programa=[]
        with open('Fons_comu/model.txt') as f:
            linies = f.readlines()
            for linia in linies:
                guio=linia.rstrip("\n")
                self.programa.append(guio)
                activitat=self.instanciar(str(index)+","+linia)
                self._llistaActivitats.append(activitat)
                index=index+1
                #Aquest codi és pot millorar segur, però cadascú hauria de poder identificar el nom de la seva activitat
       
    def temps(self):
        return self._tempsSimulacio
    
    #A completar per cadascun de vosaltres, potser trobeu alguna opció més bònica de fer-ho.
    def instanciar(self,activitat):
        element=None
        creat=False
        if 'block' in activitat:
            creat=True
            element=blockActivity(self,activitat)
        if 'batch' in activitat:
            creat=True
            element=batch(self,activitat)
        if not creat:
            element=nopActivity(self,activitat)
        
        return element
    
    def iniciSimulacio(self):
        for activitat in self._llistaActivitats:
            activitat.iniciSimulacio()

    def tractarEsdeveniment(self,esdevenimentActual):
        if (esdevenimentActual.tipus==TipusEvent.IniciSimulacio):
            self.iniciSimulacio()
            #puc programar un o més traspasEntitat al meu objecte
            self.afegirEsdeveniment(esdeveniment(self._llistaActivitats[0],0,TipusEvent.TraspasEntitat,entitat(),0,0))
            self.afegirEsdeveniment(esdeveniment(self._llistaActivitats[0],10,TipusEvent.TraspasEntitat,entitat(),0,0))
            self.afegirEsdeveniment(esdeveniment(self._llistaActivitats[0],20,TipusEvent.TraspasEntitat,entitat(),0,0))
            
    def fiSimulacio(self):
        for activitat in self._llistaActivitats:
            activitat.fiSimulacio()
   
