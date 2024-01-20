from slam import *
from queue import *
from entitat import entitat
from motorEventsDiscrets import *

class match(slamiii):

    def __init__(self, scheduler, parametres):
        super(match, self).__init__(scheduler, parametres)

        parameters = parametres
        llista_atributs = parameters.split(',')

        self.atr = int(llista_atributs[2])
        self.DST1 = int(llista_atributs[3])
        self.DST2 = int(llista_atributs[4])

        # Llista per a emmagatzemar els valors de l'entitat que entra i de la primera entitat en espera quan
        # aquests dos valors són iguals en la posició atr
        self.values_found = []

        # Llista per a emmagatzemar els ids de l'entitat que entra i de la primera entitat en espera quan
        # els seus dos corresponents valors són iguals en la posició atr
        self.entities_found = []

        # Nombre d'entitats que entren al match
        self.processed_entities = 0

        # Posem l'estat con a lliure perquè entrin les entitats
        self.set_estat(Estat.LLIURE)

        # Cua per emmagatzemar entitats en espera
        self.queue_wait = Queue() 

        # Obtenció activitats mitjançant el seu id
        self._DST1 = self.scheduler.donamActivitat(self.DST1)
        self._DST2 = self.scheduler.donamActivitat(self.DST2)


    def __repr__(self):
        return "match"

    def tractarEsdeveniment(self, event):
        '''
        Si estic LLIURE i arriba una entitat, comprovo si hi ha alguna entitat en espera amb el mateix valor a l'atribut ATR.
        - Si sí, passo a l'estat matching i passo l'entitat en espera per DST1 i l'entitat actual per DST2.
        - Si no, poso l'entitat actual en espera.
        '''
        self.entities_found = [] 
        self.values_found = [] 
        if self.get_estat() == Estat.LLIURE:
            self.processed_entities += 1
            entities_to_process = []  # Llista per a emmagatzemar les entitats que no coincideixen
            found = False

            while not self.queue_wait.empty() and not found:
                entity_wait= self.queue_wait.get()

                # Verificar si tenen el mateix valor en l'atribut ATR
                if event.entitat.get_atribut(self.atr) == entity_wait.get_atribut(self.atr):
                    self.set_estat(Estat.MATCHING)
                    self.traspassarEntitat(event.entitat, self._DST2)
                    self.traspassarEntitat(entity_wait, self._DST1)
                    self.values_found.append(event.entitat.get_atribut(self.atr))
                    self.values_found.append(entity_wait.get_atribut(self.atr))
                    self.entities_found.append(event.entitat.get_id())
                    self.entities_found.append(entity_wait.get_id())
                    # Torna a l'estat LLIURE després de processar les entitats
                    self.set_estat(Estat.LLIURE)
                    found = True # Acabar el bucle
                
                else:
                    entities_to_process.append(entity_wait)

            # Tornar a posar les entitats no coincidents a la cua
            for entity_wait in entities_to_process:
                self.queue_wait.put(entity_wait)
            
            # Si no s'ha trobat cap entitat en espera coindident amb l'entitat entrant afegir aquesta última a la cua
            if not found:
                self.queue_wait.put(event.entitat)

    def iniciSimulacio(self):
        super(match, self).iniciSimulacio()

        self.values_found = []
        self.entities_found = []

        self.processed_entities = 0

        self.set_estat(Estat.LLIURE)
        
        self.queue_wait = Queue()

    def fiSimulacio(self):
        super(match, self).fiSimulacio()

    def acceptaEntitat(self, n):
        return self.get_estat() == Estat.LLIURE

    def summary(self):
        return " EST -> " + str(self.processed_entities) + ' entitats totals, coincideixen: ' + str(
            self.entities_found) + ' amb valors ' + str(self.values_found) + ' a activitats ' + str(self._DST2) + ' ' + str(self._DST1)
