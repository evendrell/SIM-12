from enumeracions import *

class esdeveniment:
    def __init__(self,perA,temps,tipus,entitat=None,desde=None):
            # inicialitzar element de simulacio
        self.entitatsTractades=0
        self.tipus=tipus
        self.perA=perA
        self.tempsExecucio=temps
        self.entitat=entitat
        self.desde=desde

    def __repr__(self):
        return str(self.tempsExecucio)+' '+str(self.type)

    def __gt__(self, esdeveniment):
        return self.tempsExecucio > esdeveniment.tempsExecucio