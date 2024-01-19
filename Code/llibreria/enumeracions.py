from enum import Enum

#Amplieu amb aquells estats que detecteu per a cada objecte
class Estat(Enum):
    LLIURE = 1
    SERVEI = 2
    BLOQUEJAT = 3
    BATCHING = 4
    RESOURCING = 5
    DESTROYED = 6
    MATCHING = 7
    UNBATCHING = 8
    OBERTA = 240
    TANCADA = 241
#Amplieu amb aquells tipus d'events que considereu necessaris.
class TipusEvent(Enum):
    IniciSimulacio=1
    FiSimulacio=2
    TraspasEntitat=3
    CreaMentitats=4
    RepEntitat=5
    ObrirMoveEnTTics = 180
    ObrirPorta=240
    TancarPorta=241
    ObrirPortaEnTTics=242
    EstaLaPortaOberta=243 #Aquest event el genera la porta per a preguntar si està oberta
    EsticOberta=244

#Amplieu per si voleu usar alhora de treure una traça dels events.
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKRARO= '\033[97m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
