from slam import *
from queue import Queue
from entitat import *

class Select(slamiii):
    def __init__(self, scheduler, parametres):
        super(Select, self).__init__(scheduler, parametres)
        self.parametres = parametres
        lista_atributos = parametres.split(',')
        self.n = int(lista_atributos[2])
        self.frm1 = lista_atributos[3]
        self.frm2 = lista_atributos[4]
        self.last_attribute = lista_atributos[5]
        self.m = int(lista_atributos[6])
        self.set_estat(Estat.LLIURE)
        self.novaEntitat = None
        self.entitatsProcesades = 0
        self.estadisticProcessades = 0
        self.estadisticCreades = 0
        self.cola_frm1 = Queue()  # Cola para entidades de frm1
        self.cola_frm2 = Queue()  # Cola para entidades de frm2

    def __repr__(self):
        return "select"

    def actualitzarAtributs(self, entitat):
        if self.last_attribute in entitat.atributs:
            self.novaEntitat.atributs[self.last_attribute] = entitat.atributs[self.last_attribute]

    def tractarEsdeveniment(self, event):
        if self.get_estat() == Estat.LLIURE:
            if event.tipus == TipusEvent.TraspasEntitat:
                # Pull de las colas frm1 y frm2
                for _ in range(self.n):
                    self.cola_frm1.put(self.pull_entidad(self.frm1))
                    self.cola_frm2.put(self.pull_entidad(self.frm2))


                # Hago cola y acumulo entidades
                self.novaEntitat = entitat()
                self.entitatsProcesades = 1
                self.estadisticProcessades += 1
                self.set_estat(Estat.SELECTING)

        elif self.get_estat() == Estat.SELECTING:
            if event.tipus == TipusEvent.TraspasEntitat:
                self.actualitzarAtributs(event.entitat)

                self.entitatsProcesades += 1
                self.estadisticProcessades += 1
                if self.entitatsProcesades == self.n:
                    self.estadisticCreades += 1

                    # Arribat a aquest punt, hem processat n entitats
                    self.traspassarEntitat(self.novaEntitat, self._successor)
                    self.set_estat(Estat.LLIURE)

        elif self.get_estat() == Estat.CreaMentitats:
            for _ in range(self.m):
                self.traspassarEntitat(self.novaEntitat, self._successor)
                self.set_estat(Estat.LLIURE)

    def pull_entidad(self, cola):
        # Lógica para extraer una entidad de la cola especificada
        if cola:
            return cola.pop(0)  # Extracción FIFO (primero en entrar, primero en salir)
        else:
            return None  # Manejo de cola vacía

    def iniciSimulacio(self):
        super(Select, self).iniciSimulacio()
        # Posar els estadístics a zero
        self.entitatsProcesades = 0
        self.estadisticProcessades = 0
        self.estadisticCreades = 0

    def fiSimulacio(self):
        super(Select, self).fiSimulacio()

    def acceptaEntitat(self, n):
        # Suposant que ho accepto tot
        return n

    def summary(self):
        return " EST: " + str(self.estadisticProcessades) + ' ' + str(self.estadisticCreades)
