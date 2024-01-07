from slam import *





class move(slamiii):
    entren=0
     # conèixer el motor de simulació pot anar molt bé
    def __init__(self,scheduler,parametres):
        super(move, self).__init__(scheduler,parametres)

        self.parametres=parametres
        parametres_list = parametres.split(',')

        # Nombre de tics
        self.T = int(parametres_list[2])
        self.Gate = parametres_list[3]


        #Objectes que tenen entitats pendents d'entrar al move
        self.pendent_entities_buffer = []

        # Actualitzem estat inicial
        # Usem Lliure i Servei en comptes d'IDLE i WAITING
        self.set_estat(Estat.LLIURE)

        #estadistics
        self.entrades = 0
        self.sortidesGate = 0
        self.sortidesMove = 0
        
    def __repr__(self):
        return "move "+str(self.id())

    def avisarAgentesDelBufferDeEntidadesPendientes(self):
        for objecteSim in self.pendent_entities_buffer:
            objecteSim.traspasHabilitat(self, 1)
        
    def tractarEsdeveniment(self, event):
        currentState = self.get_estat()

        if currentState == Estat.LLIURE:

            #Si ens arriba una entitat...
            if event.tipus == TipusEvent.TraspasEntitat:
                # print("ENTITY ARRIVES")

                self.entrades+=1

                #programem el obriment de la GATE
                intentarEntrarAPorta = esdeveniment(perA=self.Gate, temps=self.scheduler.temps(), tipus=TipusEvent.EstaLaPortaOberta,
                                       entitat=event.entitat, desde=self, prioritat=0)
                self.scheduler.afegirEsdeveniment(intentarEntrarAPorta)

                #programem el obriment del MOVE (self) en T ticks
                obrirSelfEnTtics = esdeveniment(perA=self, temps=self.scheduler.temps() + self.T,
                                                    tipus=TipusEvent.ObrirMoveEnTTics,
                                                    entitat=event.entitat, desde=self)
                self.scheduler.afegirEsdeveniment(obrirSelfEnTtics)

                # Actualitzem estat a servei
                self.set_estat(Estat.SERVEI)

        elif currentState == Estat.SERVEI:
            if event.tipus == TipusEvent.EsticOberta:
                # Si la porta està oberta, li traspasso l'entitat
                self.traspassarEntitat(event.entitat, self.Gate)


                # Actualitzem estat a lliure
                self.set_estat(Estat.LLIURE)
                self.avisarAgentesDelBufferDeEntidadesPendientes()

                self.sortidesGate += 1

            elif event.tipus == TipusEvent.ObrirMoveEnTTics:
                # Si han passat els T ticks, traspasso l'entitat al següent
                self.traspassarEntitat(event.entitat, self._successor)
                print("Soc Move i ha passat una entitat al següent")

                # Actualitzem estat a lliure
                self.set_estat(Estat.LLIURE)
                self.avisarAgentesDelBufferDeEntidadesPendientes()

                self.sortidesMove += 1

            #Si mentres estic ocupat tractant una entitat, n'entra una altra
            elif event.tipus == TipusEvent.TraspasEntitat:
                self.pendent_entities_buffer.append(event.desde)


    def iniciSimulacio(self):
        super(move, self).iniciSimulacio()
        self.entrades=0
        self.sortidesGate=0
        self.sortidesMove=0
        self.set_estat(Estat.LLIURE)
        print('Soc move i he rebut un iniciSimulacio')

    def fiSimulacio(self):
        super(move,self).fiSimulacio()
 
    def acceptaEntitat(self, n):
        #aquí estic suposant que ho accepto tot, us convenç?
        if (self.get_estat()== Estat.SERVEI):
            return True
        return False
    
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        return " EST --> entrades: "+str(self.entrades)+' | sortides a Gate: '+str(self.sortidesGate)+' | sortides normals (continuació del flux): '+str(self.sortidesMove)

    def set_gate_reference(self, global_gate_reference):
        self.Gate = global_gate_reference
        
