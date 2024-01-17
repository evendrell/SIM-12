from slam import *
from entitat import *

class assign(slamiii):

    def __init__(self, scheduler, parametres):
        super(assign, self).__init__(scheduler, parametres)
        self.parametres = parametres
        llista_atributs = parametres.split(',')
        self.M = llista_atributs[-1]
        self.estadisticProcesats = 0
        self.estadisticCreats = 0
        self.set_estat(Estat.LLIURE)

    def __repr__(self):
        return "assign"
    
    def parse_params(self,parametres):
        params_list = parametres.split(',')
        params_dict = {}

        for param in params_list:
            key, value = param.split('=')
            params_dict[key.strip()] = value.strip()

        return params_dict

    def tractarEsdeveniment(self, event):
        for key, value in self.params_dict.items():
            event.entitat.assign_value(key, value)
            pass
        pass

    def fiSimulacio(self):
        pass

    def acceptaEntitat(self, n):
        return True  

    def summary(self):
        return " EST: " + str(self.estadisticProcesats) + ' ' + str(self.estadisticCreats)
