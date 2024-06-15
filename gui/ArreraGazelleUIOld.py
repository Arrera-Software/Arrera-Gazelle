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

        #cadre interne a l'acceuil
        self.__cadresPresentations = [
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid")]
        #Label
        self.__labelTitreMenu = Label(self.__cadreMenu,text="Menu",font=("arial","20"))
        self.__labelcadresPresentations = [
            Label(self.__cadresPresentations[0],text="Gestion recherche",font=("arial","13")),
            Label(self.__cadresPresentations[1],text="Gestion meteo",font=("arial","13")),
            Label(self.__cadresPresentations[2],text="Gestion GPS",font=("arial","13")),
            Label(self.__cadresPresentations[3],text="Gestion software",font=("arial","13")),
            Label(self.__cadresPresentations[4],text="Gestion Site internet",font=("arial","13")),
            Label(self.__cadresPresentations[5],text="Gestion theme",font=("arial","13"))]
        
        self.__boutonMenu = [Button(self.__cadreMenu,font=("arial","15"),text="Acceuil"),
                        Button(self.__cadreMenu,font=("arial","15"),text="Utilisateur"),
                        Button(self.__cadreMenu,font=("arial","15"),text="Meteo"),
                        Button(self.__cadreMenu,font=("arial","15"),text="GPS"),
                        Button(self.__cadreMenu,font=("arial","15"),text="Recherche"),
                        Button(self.__cadreMenu,font=("arial","15"),text="Software"),
                        Button(self.__cadreMenu,font=("arial","15"),text="Internet"),
                        Button(self.__cadreMenu,font=("arial","15"),text="Theme"),
                        Button(self.__cadreMenu,font=("arial","15"),text="Micro"),
                        Button(self.__cadreMenu,font=("arial","15"),text="Quitter")]

        # Placement widget 
        #Cadre acceuil
        self.__cadresPresentations[0].place(x=0,y=0)
        self.__cadresPresentations[1].place(x=180,y=0)
        self.__cadresPresentations[2].place(x=0,y=200)
        self.__cadresPresentations[3].place(x=180,y=200)
        self.__cadresPresentations[4].place(x=0,y=400)
        self.__cadresPresentations[5].place(x=180,y=400)
        

        self.__labelTitreMenu.place(relx=0.5, rely=0.0, anchor="n")
        for i in range(0,5):
            self.__labelcadresPresentations[i].place(relx=0.5, rely=0.0, anchor="n")
        
        self.__boutonMenu[0].place(relx=0.2,y=50)
        self.__boutonMenu[1].place(relx=0.2,y=100)
        self.__boutonMenu[2].place(relx=0.2,y=150)
        self.__boutonMenu[3].place(relx=0.2,y=200)
        self.__boutonMenu[4].place(relx=0.2,y=250)
        self.__boutonMenu[5].place(relx=0.2,y=300)
        self.__boutonMenu[6].place(relx=0.2,y=350)
        self.__boutonMenu[7].place(relx=0.2,y=400)
        self.__boutonMenu[8].place(relx=0.2,y=450)
        self.__boutonMenu[9].place(relx=0.2,y=500)
        
    def active(self,darkMode:bool):
        if (darkMode == True) :
            nb = 1
        else : 
            nb = 0 
        self.__cadreMenu.configure(bg=self.__secondColor[nb])
        self.__cadreAcceuil.configure(bg=self.__fristColor[nb])
        self.__cadreUser.configure(bg=self.__fristColor[nb])
        self.__cadreMeteo.configure(bg=self.__fristColor[nb])
        self.__cadreGPS.configure(bg=self.__fristColor[nb])
        self.__cadreRecherche.configure(bg=self.__fristColor[nb])
        self.__cadreSoft.configure(bg=self.__fristColor[nb])
        self.__cadreInternet.configure(bg=self.__fristColor[nb])
        self.__cadreTheme.configure(bg=self.__fristColor[nb])
        self.__cadreMicro.configure(bg=self.__fristColor[nb])
        for i in range(0,6):
            self.__labelcadresPresentations[i].configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
            self.__cadresPresentations[i].configure(bg=self.__fristColor[nb])
        
        for i in range(0,10):
            self.__boutonMenu[i].configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])

        self.__labelTitreMenu.configure(bg=self.__secondColor[nb],fg=self.__secondColorTexte[nb])
            
        self.__cadreAcceuil.pack(side="right")
        self.__cadreMenu.pack(side="left")
        
        