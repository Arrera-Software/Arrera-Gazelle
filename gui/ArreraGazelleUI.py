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
        # Mise de la fenetre dans un atribut
        self.__windows = windows
        # Declaration des cardre
        self.__mainCadre = Frame(self.__windows,width=500,height=400)

        # Widget 
        # Main frame 
        btnAcceuilUser = Button(self.__mainCadre,width=8,height=4,text="Utilisateur",font=("arial","15"))

        # Affichage 
        btnAcceuilUser.place(x=20,y=20)
    
    def active(self,darkMode:bool):
        if (darkMode == True) :
            nb = 1
        else : 
            nb = 0 
        self.__mainCadre.pack()