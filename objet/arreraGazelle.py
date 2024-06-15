from librairy.travailJSON import*
from librairy.dectectionOS import*
from librairy.gestionSoftWindows import*

class CArreraGazelle :
    def __init__(self,emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str):
        self.__fileJsonUser = jsonWork(emplacementJsonUser)
        self.__fileJsonNeuronNetwork = jsonWork(emplacementJsonNeuronNetwork)
        self.__fileJsonAssistant = jsonWork(emplacementJsonAssistant)
    
    def changeUserName(self,newName:str):
        self.__fileJsonUser.EcritureJSON("user",newName)
    
    def changeUserGenre(self,newGenre:str):
        self.__fileJsonUser.EcritureJSON("genre",newGenre)