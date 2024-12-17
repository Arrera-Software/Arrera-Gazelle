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

        self.__userFrame = self.__arrtk.createFrame(self.__windows,width=500,height=330)

        self.__backFrame = self.__arrtk.createFrame(self.__windows,width=500,height=70)

        # Variable
        # Taille Police
        taillePolice = 20
        # Icon Assistant
        iconAssistant = self.__arrtk.createImage(jsonSetting.lectureJSON("iconSoft"),tailleX=95,tailleY=95)

        # Widget 
        # Main frame
        btnIcon = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,image=iconAssistant)
        btnAcceuilUser = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Utilisateur"
                                                   ,ppolice="Arial",ptaille=taillePolice-2,pstyle="bold",command= lambda  : self.__viewUser())
        btnAcceuilMeteo = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Meteo"
                                                    ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilGPS = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="GPS"
                                                  ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilRecherche = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Recherche"
                                                        ,ppolice="Arial",ptaille=taillePolice-2,pstyle="bold")
        btnAcceuilLogiciel = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Logiciel"
                                                       ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilInternet = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Internet"
                                                       ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilTheme = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Theme"
                                                    ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilArreraWork = self.__arrtk.createButton(self.__mainCadre,width=100,height=100
                                                         ,text="Arrera\nWork",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilDownload = self.__arrtk.createButton(self.__mainCadre,width=100,height=100
                                                       ,text="Arrera\nDownload",ppolice="Arial",ptaille=taillePolice-2,pstyle="bold")
        btnAcceuilMicro = self.__arrtk.createButton(self.__mainCadre,width=100,height=100
                                                    ,text="Micro",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        self.__btnRetourAssistant = self.__arrtk.createButton(self.__mainCadre,width=100,
                                                              height=100,text="Retour",ppolice="Arial",ptaille=taillePolice,pstyle="bold")

        # backFrame
        retourAcceuilBTN = self.__arrtk.createButton(self.__backFrame,text="Retour Acceuil"
                                                     ,ppolice="Arial",ptaille=taillePolice,command=lambda:self.__backAcceuil())


        # userFrame
        # Label
        labelTitleUser = self.__arrtk.createLabel(self.__userFrame,text="Gestion utilisateur"
                                                  ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")

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
        # backFrame
        self.__arrtk.placeCenterRight(retourAcceuilBTN)
        # userFrame
        self.__arrtk.placeTopCenter(labelTitleUser)
    
    def active(self):
        self.__mainCadre.pack()

    def __clearAll(self):
        self.__mainCadre.pack_forget()
        self.__userFrame.pack_forget()
        self.__backFrame.pack_forget()

    def __viewUser(self):
        self.__clearAll()
        self.__userFrame.pack()
        self.__backFrame.pack()

    def __backAcceuil(self):
        self.__clearAll()
        self.__mainCadre.pack()