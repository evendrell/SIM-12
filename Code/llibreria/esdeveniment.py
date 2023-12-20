from enumeracions import *

class esdeveniment:
    def __init__(self,perA,temps,tipus,entitat=None,desde=None,prioritat=1):
            # inicialitzar element de simulacio
        self.tipus=tipus
        self.perA=perA
        self.tempsExecucio=temps
        self.entitat=entitat
        self.desde=desde
        self.prioritat=prioritat

    def __repr__(self):
        return str(self.tempsExecucio)+' '+str(self.type)

    def __gt__(self, esdeveniment):
        #afegiu la prioritat com a condició d'ordenament
        return self.tempsExecucio > esdeveniment.tempsExecucio