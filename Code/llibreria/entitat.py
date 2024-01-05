class entitat():
    #estaria bé que el _id fos únic per a cada instància d'entitat
    _id=0
    
    def __init__(self,):
       #TODO Molt per fer
       
       #llista atributs...
       self.atributs = []
       return
    

    # Devuelve el atributo en la posición del índice
    def get_atribut(self, index):
        if 0 <= index < len(self.atributs): return self.atributs[index]
        else: return None
    