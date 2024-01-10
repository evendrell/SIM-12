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

        #estadistics interns
        self.entrades = 0
        self.sortidesGate = 0
        self.sortidesMove = 0
        self.entitiesThatHaveEntered = []

        #Id de la entitat que estic tractant
        # (per si mentres estic en servei amb entitat B, es dispara un event per tractar entitat A que ja havia soltat)
        self.currentEntityOrMinusOne = -1

        
    def __repr__(self):
        return "move "+str(self.id())

    def avisarAgentesDelBufferDeEntidadesPendientes(self):
        print("Soc Move i aviso a tots els agents del meu buffer: " + str(self.pendent_entities_buffer))
        for objecteSim in self.pendent_entities_buffer:
            objecteSim.traspasHabilitat(self, 1)
        self.pendent_entities_buffer = []
        
    def tractarEsdeveniment(self, event):
        currentState = self.get_estat()

        if currentState == Estat.LLIURE:

            #Si ens arriba una entitat...
            if event.tipus == TipusEvent.TraspasEntitat:

                self.currentEntityOrMinusOne = event.entitat._id
                self.entitiesThatHaveEntered.append(event.entitat._id)

                self.entrades+=1

                # Actualitzem estat a servei
                self.set_estat(Estat.SERVEI)

                # programem el obriment del MOVE (self) en T ticks
                # if self.Gate.esticOberta():
                obrirSelfEnTtics = esdeveniment(perA=self, temps=self.scheduler.temps() + self.T,
                                                tipus=TipusEvent.ObrirMoveEnTTics,
                                                entitat=event.entitat, desde=self)
                self.scheduler.afegirEsdeveniment(obrirSelfEnTtics)

                #programem el obriment de la GATE
                intentarEntrarAPorta = esdeveniment(perA=self.Gate, temps=self.scheduler.temps(), tipus=TipusEvent.EstaLaPortaOberta,
                                       entitat=event.entitat, desde=self, prioritat=0)
                self.scheduler.afegirEsdeveniment(intentarEntrarAPorta)


        elif currentState == Estat.SERVEI:
            if event.tipus == TipusEvent.EsticOberta:
                if event.entitat != None and event.entitat._id == self.currentEntityOrMinusOne:
                    # Si la porta està oberta, li traspasso l'entitat
                    self.traspassarEntitat(event.entitat, self.Gate)


                    # Actualitzem estat a lliure
                    self.set_estat(Estat.LLIURE)
                    self.avisarAgentesDelBufferDeEntidadesPendientes()
                    self.currentEntityOrMinusOne = -1

                    self.sortidesGate += 1


                else:
                    print("Soc Move i he rebut un EsticOberta d'una entitat que no és la que estic tractant")
                    pass

            elif event.tipus == TipusEvent.ObrirMoveEnTTics:
                if event.entitat != None and event.entitat._id == self.currentEntityOrMinusOne:
                    # Si han passat els T ticks, traspasso l'entitat al següent
                    self.traspassarEntitat(event.entitat, self._successor)
                    print("Soc Move i ha passat una entitat al següent")

                    # Actualitzem estat a lliure
                    self.set_estat(Estat.LLIURE)
                    self.avisarAgentesDelBufferDeEntidadesPendientes()
                    self.currentEntityOrMinusOne = -1

                    self.sortidesMove += 1
                else:
                    print("Soc Move i he rebut un ObrirMoveEnTTics d'una entitat que no és la que estic tractant")
                    pass

            #Si mentres estic ocupat tractant una entitat, n'entra una altra
            elif event.tipus == TipusEvent.TraspasEntitat:
                print("Soc Move i he rebut una entitat (id:"+str(event.entitat.get_id())+") mentre estava tractant una altra entitat")
                self.pendent_entities_buffer.append(event.desde)


    def iniciSimulacio(self):
        super(move, self).iniciSimulacio()
        self.Gate = self.scheduler.donamActivitat(int(self.Gate))
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
            return False
        return True
    
    def summary(self):
        #Pot ser una bona praxis disposar d'un resum del que ha fet el vostre element al llarg de tota l'execució
        return " EST --> entr: "+str(self.entrades)+' | sort.G: '+str(self.sortidesGate)+' | sort.N: '+str(self.sortidesMove) + ' | entidades +' + str(self.entitiesThatHaveEntered)

    def set_gate_reference(self, global_gate_reference):
        # print("Soc move i he rebut una referència a la porta: " + str(global_gate_reference))
        self.Gate = global_gate_reference

