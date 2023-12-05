import random

class Bil:
    def __init__(self,temps):
        #Carrer a on arribara
        self.carrer=(int)(random.uniform(0,4))
        self.gainTime=temps
        self.livstid=0
        pass

    def gaut(self,temps):
        self.livstid=temps-self.gainTime
