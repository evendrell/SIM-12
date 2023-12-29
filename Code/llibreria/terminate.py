from slam import *
from queue import Queue
from entitat import *
from esdeveniment import esdeveniment

class terminate(slamiii):
    def __init__(self,scheduler,parametres):
        super(batch, self).__init__(scheduler, parametres)
        self.parametres=parametres
        lista_atributos = parametres.split(',')
        self.tc = int(lista_atributos[2])

    def terminate(self):
        if self.TC is not None and self.TC > 0:
            # if tc>0 aturar simulació
            self.scheduler.aturarSimulacio()
        else:
            # else eliminar esdeveniment (???)
            self.scheduler.eliminarEsdeveniment() 