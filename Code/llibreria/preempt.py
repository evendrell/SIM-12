from slam import *
from queue import Queue
from entitat import entitat
from motorEventsDiscrets import *

class Preempt():
    def __init__(self, ifl, priority, resource, snlbl = None, natr = None, m = None):
        self.ifl = ifl
        self.priority = priority
        self.resource = resource
        self.snlbl = snlbl
        self.natr = natr
        self.m = m
        self.seized_entities = []

    def seize_resource(self, entity_priority):
        # Lógica para prevenir el recurso
        # Comprueba la prioridad, la capacidad del recurso, etc.
        if self.priority == "HIGH(NATR)":  # Si es alta prioridad
            if not self.seized_entities:  # Si no hay entidades en cola
                self.seized_entities.append(entity_priority)
                return "Resource seized"
            else:
                if entity_priority > self.seized_entities[0]:
                    self.seized_entities.insert(0, entity_priority)
                    return "Resource seized with preemption"
                else:
                    return "Entity priority not high enough for preemption"
        elif self.priority == "LOW(NATR)":  # Si es baja prioridad
            self.seized_entities.append(entity_priority)
            return "Resource seized"

    def release_resource(self):
        # Lógica para liberar el recurso
        if self.seized_entities:
            return self.seized_entities.pop(0)
        else:
            return "No entity to release"
