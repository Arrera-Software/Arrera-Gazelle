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
    
    def ajoutVilleMeteo(self,mode:int,ville:str):
        """
        1 : domicile
        2 : Travail 
        3 : Autre
        """
        if (mode == 1 ):
            self.__fileJsonUser.EcritureJSON("lieuDomicile",ville)
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.EcritureJSON("lieuTravail",ville)
                return True
            else :
                if (mode==3):
                    self.__fileJsonUser.EcritureJSONList("listVille",ville)
                    return True
                else :
                    return False
    
    def supprVilleMeteo(self,mode:int,ville:str):
        """
        1 : domicile
        2 : Travail 
        3 : Autre
        """
        if (mode == 1 ):
            self.__fileJsonUser.suppressionJson("lieuDomicile")
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.suppressionJson("lieuTravail")
                return True
            else :
                if ((mode==3)and(ville != "")):
                    self.__fileJsonUser.suppressionJsonList("listVille",ville)
                    return True
                else :
                    return False
    
    def getMeteoSave(self):
        listeMeteo = []
        if (self.__fileJsonUser.lectureJSON("lieuDomicile") != ""):
            listeMeteo.append("Lieu d'habitation enregister")

        if (self.__fileJsonUser.lectureJSON("lieuTravail") != ""):
            listeMeteo.append("Lieu de travail enregister")
        
        listeMeteo = listeMeteo+self.__fileJsonUser.lectureJSONList("listVille")

        return listeMeteo

    def ajoutGPSAdresse(self,mode:int,adresse:str):
        """
        1 : Adresse domicile
        2 : Adresse lieu de travail
        """
        if (mode==1):
            self.__fileJsonUser.EcritureJSON("adresseDomicile",adresse)
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.EcritureJSON("adresseTravail",adresse)
                return True
            else :
                return False
    
    def supprGPSAdresse(self,mode:int):
        """
        1 : Adresse domicile
        2 : Adresse lieu de travail
        """
        if (mode==1):
            self.__fileJsonUser.suppressionJson("adresseDomicile")
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.suppressionJson("adresseTravail")
                return True
            else :
                return False