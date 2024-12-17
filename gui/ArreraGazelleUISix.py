from librairy.arrera_tk import *
from objet.arreraGazelle import*
from typing import Union

class CArreraGazelleUISix :
    def __init__(self,arrTK:CArreraTK,windows:Union[ctk.CTk,ctk.CTkToplevel],emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str,emplacementConfigSetting:str):
        # Ouverture de l'objet
        self.__gazelle = CArreraGazelle(emplacementJsonUser,emplacementJsonNeuronNetwork,emplacementJsonAssistant)
        jsonSetting = jsonWork(emplacementConfigSetting)

        # Mise de la fenetre dans un atribut
        self.__windows = windows
        self.__arrtk = arrTK
        # Declaration des cardre
        self.__mainCadre = self.__arrtk.createFrame(self.__windows,width=500,height=400)

        # Variable
        # Taille Police
        taillePolice = 20
        # Icon Assistant
        iconAssistant = self.__arrtk.createImage(jsonSetting.lectureJSON("iconSoft"),tailleX=95,tailleY=95)

        # Widget 
        # Main frame
        btnIcon = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,image=iconAssistant)
        btnAcceuilUser = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Utilisateur",ppolice="Arial",ptaille=taillePolice-2,pstyle="bold")
        btnAcceuilMeteo = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Meteo",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilGPS = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="GPS",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilRecherche = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Recherche",ppolice="Arial",ptaille=taillePolice-2,pstyle="bold")
        btnAcceuilLogiciel = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Logiciel",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilInternet = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Internet",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilTheme = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Theme",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilArreraWork = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Arrera\nWork",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilDownload = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Arrera\nDownload",ppolice="Arial",ptaille=taillePolice-2,pstyle="bold")
        btnAcceuilMicro = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Micro",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        self.__btnRetourAssistant = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Retour",ppolice="Arial",ptaille=taillePolice,pstyle="bold")


        # Affichage 
        btnIcon.place(x=20,y=20)
        btnAcceuilUser.place(x=140,y=20)
        btnAcceuilMeteo.place(x=260,y=20)
        btnAcceuilGPS.place(x=380,y=20)
        btnAcceuilRecherche.place(x=20,y=140)
        btnAcceuilLogiciel.place(x=140,y=140)
        btnAcceuilInternet.place(x=260,y=140)
        btnAcceuilTheme.place(x=380,y=140)
        btnAcceuilArreraWork.place(x=20,y=260)
        btnAcceuilDownload.place(x=140,y=260)
        btnAcceuilMicro.place(x=260,y=260)
        self.__btnRetourAssistant.place(x=380,y=260)
    
    def active(self):
        self.__mainCadre.pack()