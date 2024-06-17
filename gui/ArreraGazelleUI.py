from tkinter import*
from objet.arreraGazelle import*
from tkinter.messagebox import*
from typing import Union

class CArreraGazelleUI :
    def __init__(self,windows:Union[Tk,Toplevel],emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str,emplacementConfigSetting:str):
        # Ouverture de l'objet
        self.__gazelle = CArreraGazelle(emplacementJsonUser,emplacementJsonNeuronNetwork,emplacementJsonAssistant)
        jsonSetting = jsonWork(emplacementConfigSetting)
        # recuperation color
        self.__listMainColor = [jsonSetting.lectureJSON("lightColor"),jsonSetting.lectureJSON("darkColor")]
        self.__listMainTextColor = [jsonSetting.lectureJSON("lightTextColor"),jsonSetting.lectureJSON("darkTextColor")]
    
    def active(self,darkMode:bool):
        if (darkMode == True) :
            nb = 1
        else : 
            nb = 0 