from entitatIdFactory import entitatIdFactory
class entitat():
    #estaria bé que el _id fos únic per a cada instància d'entitat
    _id=0

    def __init__(self,):
        #Inicialitzem el id de l'entitat
        idFactory = entitatIdFactory()
        self._id = entitatIdFactory.get_id(idFactory)

        # Inicialitzem llista d'atributs
        self.atributs = []
        return

    def get_id(self):
        return self._id

    # Devuelve el atributo en la posición del índice
    def get_atribut(self, index):
        if 0 <= index < len(self.atributs): return self.atributs[index]
        else: return None
    