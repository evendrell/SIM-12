from slam import *
from entitat import entitat
from motorEventsDiscrets import *

class free(slamiii):
    
    def __init__(self, scheduler, parametres):
        super(free, self).__init__(scheduler, parametres)
        self.set_estat(Estat.LLIURE)
        self.entitatsProcesades = 0
        self.entitatsCreades = 0
        self.parametres=parametres
        llista_atributs = parametres.split(',')

        self.resource = int(llista_atributs[0])
        self.units = int(llista_atributs[1])
        self.M = int(llista_atributs[2])
        
    def __repr__(self):
        return "free"
    
    def tractarEsdeveniment(self, event):

        if event.tipus == TipusEvent.TraspasEntitat:
            self.process_entity(event.entitat)
    
    def process_entity(self, entitat):
        # Assuming entitat.resource and entitat.units_to_free store the necessary information
        resource = entitat.get_atribut(self.resource)  # The resource to free units from
        units_to_free = entitat.get_atribut(self.units)  # The number of units to free
        M = entitat.get_atribut(self.M)  # The parameter for creating additional entities
        
        # Implement the logic to free units from the resource
        self.free_resource_units(resource, units_to_free)
        
        # Create additional entities if M > 0
        if M > 0:
            self.create_additional_entities(M)
        
        self.traspassarEntitat(entitat, self._successor)
        self.entitatsProcesades += 1

    def free_resource_units(self, resource, units_to_free):
        # Here you would free the specified units from the resource
        resource.free_units(units_to_free)
        pass
    
    def create_additional_entities(self, M):
        for _ in range(M):
            new_entity = entitat()
            self.traspassarEntitat(new_entity, self._successor)
            self.entitatsCreades += 1

    def iniciSimulacio(self):
        super(free, self).iniciSimulacio()
        pass
    
    def fiSimulacio(self):
        super(free, self).fiSimulacio()
        pass

    def acceptaEntitat(self, n):
        self.acceptaEntitat(n)
        pass

    def summary(self):
        #Mostrar els estadístics per pantalla amb el nom, format desitjat 
        return " EST: "+str(self.entitatsProcesades)+' '+str(self.entitatsCreades)