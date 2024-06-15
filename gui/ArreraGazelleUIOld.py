from tkinter import*
from objet.arreraGazelle import*
from typing import Union

class CArreraGazelleUI :
    def __init__(self,windows:Union[Tk,Toplevel],emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str,emplacementConfigSetting:str):
        # Ouverture de l'objet
        self.__gazelle = CArreraGazelle(emplacementJsonUser,emplacementJsonNeuronNetwork,emplacementJsonAssistant)
        jsonSetting = jsonWork(emplacementConfigSetting)
        # Recuperation des variable pour les couleur
        self.__fristColor = [jsonSetting.lectureJSON("colorLight1"),jsonSetting.lectureJSON("colorDark1")]
        self.__secondColor = [jsonSetting.lectureJSON("colorLight2"),jsonSetting.lectureJSON("colorDark2")]
        self.__fristColorTexte = [jsonSetting.lectureJSON("textColorLight1"),jsonSetting.lectureJSON("textColorDark1")]
        self.__secondColorTexte = [jsonSetting.lectureJSON("textColorLight2"),jsonSetting.lectureJSON("textColorDark2")]
        # Mise de la fenetre dans un atribut
        self.__windows = windows
        # Creation des Frame
        self.__cadreMenu = Frame(self.__windows,width=150,height=600)
        self.__cadreAcceuil = Frame(self.__windows,width=350,height=600)
        self.__cadreUser = Frame(self.__windows,width=350,height=600)
        self.__cadreMeteo = Frame(self.__windows,width=350,height=600)
        self.__cadreGPS = Frame(self.__windows,width=350,height=600)
        self.__cadreRecherche = Frame(self.__windows,width=350,height=600)
        self.__cadreSoft = Frame(self.__windows,width=350,height=600)
        self.__cadreInternet = Frame(self.__windows,width=350,height=600)
        self.__cadreTheme = Frame(self.__windows,width=350,height=600)
        self.__cadreMicro = Frame(self.__windows,width=350,height=600)
        
    def active(self,darkMode:bool):
        if (darkMode == True) :
            self.__cadreMenu.configure(bg=self.__secondColor[1])
            self.__cadreAcceuil.configure(bg=self.__fristColor[1])
            self.__cadreUser.configure(bg=self.__fristColor[1])
            self.__cadreMeteo.configure(bg=self.__fristColor[1])
            self.__cadreGPS.configure(bg=self.__fristColor[1])
            self.__cadreRecherche.configure(bg=self.__fristColor[1])
            self.__cadreSoft.configure(bg=self.__fristColor[1])
            self.__cadreInternet.configure(bg=self.__fristColor[1])
            self.__cadreTheme.configure(bg=self.__fristColor[1])
            self.__cadreMicro.configure(bg=self.__fristColor[1])
        else : 
            self.__cadreMenu.configure(bg=self.__secondColor[0])
            self.__cadreAcceuil.configure(bg=self.__fristColor[0])
            self.__cadreUser.configure(bg=self.__fristColor[0])
            self.__cadreMeteo.configure(bg=self.__fristColor[0])
            self.__cadreGPS.configure(bg=self.__fristColor[0])
            self.__cadreRecherche.configure(bg=self.__fristColor[0])
            self.__cadreSoft.configure(bg=self.__fristColor[0])
            self.__cadreInternet.configure(bg=self.__fristColor[0])
            self.__cadreTheme.configure(bg=self.__fristColor[0])
            self.__cadreMicro.configure(bg=self.__fristColor[0])
    
        self.__cadreAcceuil.pack(side="right")
        self.__cadreMenu.pack(side="left")
        
        